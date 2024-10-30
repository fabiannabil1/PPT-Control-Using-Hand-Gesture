import cv2
import mediapipe as mp
import asyncio
import time  # Tambahkan modul time untuk penghitungan waktu
from pynput.keyboard import Controller, Key

keyboard = Controller()

# Inisialisasi MediaPipe untuk deteksi tangan
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7)

# Deklarasi variabel state di level global
prev_finger_count = None
last_change_time = time.time()  # Waktu terakhir kali posisi jari berubah

# Fungsi untuk menghitung jumlah jari yang terangkat
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Indeks landmark ujung jari (telunjuk - kelingking)
    thumb_tip = 4  # Indeks ujung ibu jari
    count = 0

    # Ibu jari: posisinya berbeda dari jari lain
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 2].x:
        count += 1

    # Hitung jari telunjuk hingga kelingking
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1

    return count

async def main():
    global prev_finger_count, last_change_time  # Deklarasi global

    cap = cv2.VideoCapture(0)  # Gunakan kamera

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Konversi frame ke RGB untuk MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Hitung jumlah jari yang terangkat
                finger_count = count_fingers(hand_landmarks)

                # Cek apakah ada perubahan jumlah jari
                if finger_count != prev_finger_count:
                    # Reset timer saat jumlah jari berubah
                    last_change_time = time.time()
                    prev_finger_count = finger_count

                # Cek jika posisi jari bertahan lebih dari 300 ms
                elif time.time() - last_change_time >= 0.3:
                    if finger_count == 0:
                        keyboard.press(Key.right)
                        keyboard.release(Key.right)
                    elif finger_count == 2:
                        keyboard.press(Key.left)
                        keyboard.release(Key.left)

                    # Reset timer agar event tidak terus terjadi
                    last_change_time = time.time()

        # Tampilkan frame dengan deteksi tangan
        cv2.imshow("Hand Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Jalankan program
if __name__ == "__main__":
    asyncio.run(main())

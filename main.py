from oled_face import OledFaceController

def main():
    oled = OledFaceController()
    try:
        oled.blink_eyes()
    except KeyboardInterrupt:
        oled.cleanup()

if __name__ == "__main__":
    main()
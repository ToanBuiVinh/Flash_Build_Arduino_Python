import subprocess
import sys

# Cấu hình thông tin
BOARD_FQBN = "arduino:avr:uno"
PORT = "COM5"  # Thay bằng cổng thực tế Arduino của bạn
SKETCH_PATH = r"C:\Users\admin\Downloads\Blink\Blink.ino"  # Đường dẫn chứa file .ino

def run_cmd(cmd):
    print(f"🔹 Chạy lệnh: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ Lỗi: {result.stderr}")
        sys.exit(1)

def main():
    print("✅ Bắt đầu build và upload Arduino...")

    # Bước 1: Compile code
    run_cmd(f'arduino-cli compile --fqbn {BOARD_FQBN} "{SKETCH_PATH}"')

    # Bước 2: Upload code
    run_cmd(f'arduino-cli upload -p {PORT} --fqbn {BOARD_FQBN} "{SKETCH_PATH}"')

    print("🎉 Upload hoàn tất thành công!")

if __name__ == "__main__":
    main()

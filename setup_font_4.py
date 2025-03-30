import os
import subprocess
import sys
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 1️⃣ Colab 환경인지 확인
if "google.colab" in sys.modules:
    from google.colab import drive
    print("🔹 Google Colab 환경이 감지되었습니다. Google Drive를 마운트합니다.")
    drive.mount('/content/drive', force_remount=True)
    font_dir = "/content/drive/MyDrive/fonts"
else:
    print("🔸 Colab 환경이 아닙니다. 로컬 저장소를 사용합니다.")
    font_dir = os.path.expanduser("~/.fonts")  # 로컬 환경에서는 ~/.fonts 사용

# 2️⃣ 폰트 저장 경로 설정
os.makedirs(font_dir, exist_ok=True)
font_path = os.path.join(font_dir, "NanumGothic.ttf")

# 3️⃣ 폰트 다운로드 (없으면 다운로드)
if not os.path.exists(font_path):
    print("⏳ NanumGothic.ttf 다운로드 중...")
    subprocess.run(["wget", "-O", font_path, "https://hangeul.pstatic.net/hangeul_static/webfont/NanumGothic/NanumGothic.ttf"], check=True)
    print("✅ 폰트 다운로드 완료!")
else:
    print("🔹 기존 폰트 사용")

# 4️⃣ Matplotlib에 폰트 적용
fm.fontManager.addfont(font_path)
fontprop = fm.FontProperties(fname=font_path)

# 5️⃣ 기본 폰트 설정
plt.rc('font', family=fontprop.get_name())
sns.set(font=fontprop.get_name())

# 6️⃣ 폰트 캐시 갱신 (업데이트된 방식 사용)
fm._load_fontmanager()

# 7️⃣ Colab에서는 폰트 캐시 삭제 후 다시 로드해야 적용됨
if "google.colab" in sys.modules:
    print("🔄 Matplotlib 캐시 삭제 후 재시작 필요 (Colab 환경)")
    subprocess.run(["rm", "-rf", "/root/.cache/matplotlib"], check=True)

print("🎉 한글 폰트가 성공적으로 적용되었습니다! ✅")

# 8️⃣ 테스트 출력
plt.figure(figsize=(4, 2))
plt.text(0.5, 0.5, "한글 테스트 성공!", fontsize=20, ha='center', va='center')
plt.show()
import subprocess
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from google.colab import drive

# 1️⃣ Google Drive 마운트
drive.mount('/content/drive', force_remount=True)

# 2️⃣ 폰트 저장 경로 설정 (Google Drive에 저장)
font_dir = os.path.join('/content/drive/MyDrive/', "fonts")
os.makedirs(font_dir, exist_ok = True)
font_path = os.path.join(font_dir, "NanumGothic.ttf")

# 3️⃣ 폰트 다운로드 (없으면 다운로드)
if not os.path.exists(font_path):
    print("다운로드 NanumGothic.ttf...")
    subprocess.run(["wget", "-O", font_path, "https://hangeul.pstatic.net/hangeul_static/webfont/NanumGothic/NanumGothic.ttf"])
    print("✅ 폰트 다운로드 완료!")
else:
    print("🔹 기존 폰트 사용")

# 4️⃣ Matplotlib에 폰트 적용
fm.fontManager.addfont(font_path)
# fontprop = fm.FontProperties(fname=font_path)

# 5️⃣ 기본 폰트 설정
# plt.rc('font', family=fontprop.get_name()) 수정전
plt.rc('font', family='NanumGothic')

# 6️⃣ Seaborn에도 적용
# sns.set(font=fontprop.get_name()) 수정전
sns.set(font='Nanumgothic')

# 7️⃣ 폰트 캐시 갱신
# fm._load_fontmanager()

print("🎉 한글 폰트가 성공적으로 적용되었습니다! ✅")

# Call setup_font() when the script is run
if __name__ == "__main__":
  # If we are in a Google Colab environment, attempt mounting.
  if 'google.colab' in sys.modules:
      try:
          google.colab.drive.mount('/content/drive', force_remount=True)
      except AttributeError:
          # Ignore AttributeError if `google.colab.drive` is unavailable
          pass
  setup_font()

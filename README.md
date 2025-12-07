<div align="center">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
 <img src="assets/gacha_machine.png">
</div>

<div align="center">

# Gacha-Widget
**Gacha-Widget**을 통해 몇 가지의 위젯을 뽑아 상호작용을 확인하세요!

</div>

## 시연 영상

<div align="center">
  <a href="https://youtu.be/8S2XWPIsWKw" target="_blank">
    <img src="https://img.youtube.com/vi/8S2XWPIsWKw/0.jpg" width="70%" />
  </a>
</div>

## 주요 위젯

| 위젯 이미지 | 설명 |
| ----- | ----- |
| <div align="center"><img src="assets/gacha_machine.png" height="80"></div> | Gacha Machine입니다. (좌클릭을 통해 위젯을 뽑을 수 있고, 우클릭을 통해 초기화 혹은 종료가 가능합니다.) |
| <div align="center"><img src="assets/asparagus.png" height="80"></div> | 아스파라거스입니다. 거북이가 좋아할 것 같습니다. |
| <div align="center"><img src="assets/ball_normal.png" height="80"></div> | 공입니다. 꽤 무겁습니다. |
| <div align="center"><img src="assets/blackhole.png" height="80"></div> | 블랙홀입니다. 무엇이든 빨려들어갑니다. |
| <div align="center"><img src="https://emoji.discourse-cdn.com/apple/clock3.png" height="80"></div> | 말 그대로 시계입니다. (실제 이미지와 다를 수 있습니다.) |
| <div align="center"><img src="assets/cloud.png" height="80"></div> | 구름입니다. 알아서 잘 돌아다닙니다. |
| <div align="center"><img src="assets/cookie_closed.png" height="80"></div> | 행운의 쿠키입니다. '뜻밖의 행운'을 찾아보세요. |
| <div align="center"><img src="assets/myturtle_normal.png" height="80"></div> | 거북이입니다. 공에 깔리지 않게 조심하세요. |
| <div align="center"><img src="assets/postit.png" height="80"></div> | 메모장입니다. 글씨가 작아 안보일지도 모릅니다. |


## 🕹️ 사용 방법 (How to Use)

1. **위젯 스폰**: 메인 **Gacha Machine** 아이콘을 마우스 **왼쪽 버튼으로 클릭**합니다. 화면에 무작위 위젯이 나타납니다.

2. **위젯 이동**: 스폰된 모든 위젯(메인 머신 포함)은 드래그하여 원하는 위치로 자유롭게 이동할 수 있습니다.

3. **위젯 상호작용**:

   * **Post-It**을 클릭하여 메모를 시작합니다.

   * **Cookie**를 클릭하여 숨겨진 메시지를 확인합니다.

   * **Turtle**에게 **Asparagus**를 드래그하여 먹이를 줍니다.

4. **위젯 삭제 및 정리**:

   * **Black Hole** 위젯을 드래그하여 다른 위젯(터틀 포함, 블랙홀끼리도 가능)과 **겹치게 하면** 해당 위젯은 블랙홀에 흡수되어 사라집니다.

   * 두 개의 **Black Hole** 위젯이 충돌하면 하나가 사라져 화면에 블랙홀이 하나만 남도록 합니다.

5. **전체 초기화**: 메인 **Gacha Machine** 아이콘을 마우스 **오른쪽 버튼으로 클릭**하여 '초기화'를 선택하면 화면의 **모든 위젯**이 즉시 사라집니다.

## 🛠️ 개발 환경 및 PyInstaller 빌드

이 애플리케이션은 **Python** 언어와 **PyQt6** 프레임워크를 기반으로 개발되어, 플랫폼 독립적인 GUI 환경을 제공합니다. Windows 환경에서 배포 및 실행의 용이성을 위해 **PyInstaller**를 사용하여 단일 실행 파일(`.exe`)로 빌드됩니다.

### 리소스 관리 (`assets` 폴더)

모든 이미지(`png`, `ico`) 파일은 프로젝트의 루트에 위치한 **`assets`** 폴더에 모여 있으며, 이는 PyInstaller가 리소스를 효율적으로 관리하고 번들에 포함시키기 위한 최적의 구조입니다.

### 실행 파일 생성 명령어 (Windows 기준)


아래 명령어는 `main.py`와 모든 리소스(`assets`)를 포함하여 단일 실행 파일을 생성합니다. 특히, `--add-data` 옵션을 통해 `assets` 폴더의 모든 내용을 번들 내부의 `assets` 경로로 정확히 매핑하여 런타임에 발생할 수 있는 리소스 누락 오류를 방지합니다.

exe 다운로드 링크 :
https://drive.google.com/file/d/1AD7sd41y9z1qHb9rLoMkDNbZ8Adlvb9T/view?usp=sharing
demo 영상 링크 :
https://youtu.be/8S2XWPIsWKw











































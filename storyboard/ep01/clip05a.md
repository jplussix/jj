# 1화 클립 5-A — 군막에서 깨어남

- 대본 위치: `scripts/ep01.md` 씬 5 앞부분 (깨어나서 물에 비친 얼굴을 보기까지)
- 길이: 30초 / 480p / 16:9
- 모델: 시댄스 2.5 (힉스필드, omni_reference)
- 참조:
  - Image 1: 한이겸 캐릭터 시트 `docs/sheets/hanigyeom.png` (job `63cb6e08-d28c-4664-af11-533a329286cb`)
  - Image 2: 군막 배경 `docs/locations/tent_a.png` (job `d21fdb03-3a84-43d0-aa8f-7d882fabf861`)
- 목소리: 이번 테스트는 시댄스 자체 음성. 목소리 참조는 다음 테스트에서.

## 대본 (이 클립 분량)

북소리.

한이겸이 눈을 뜬다. 천장이 천막이다. 벌떡 일어나 앉는다.

**한이겸**
아이고.

한이겸이 멈춘다. 허리를 만진다. 무릎을 굽혔다 편다.

**한이겸**
안 아프네.

자기 손을 본다. 주름이 없다. 굵은 팔뚝을 쥐어 본다. 배를 더듬는다. 납작하다.

놋대야의 물에 얼굴을 비춘다. 수염 난 젊은 얼굴.

**한이겸**
누구세요.

물속의 얼굴이 같은 입 모양을 한다.

## 컷 구성

| 단계 | 내용 | 화면 |
|---|---|---|
| 1 | 북소리에 벌떡 일어나 허리 짚으며 "아이고" | 미디엄숏, 눈높이 |
| 2 | 무릎 굽혀 보고 "안 아프네" | 천천히 다가가며 허리 위 |
| 3 | 손, 팔뚝, 배를 차례로 만져 봄 | 같은 숏 유지 |
| 4 | 대야에 비친 얼굴, "누구세요", 놀란 얼굴에서 멈춤 | 어깨 너머 → 얼굴 클로즈업 |

## 프롬프트

```
[Generation Goal]
A comedic historical drama clip: a young Joseon general wakes up in his army tent and slowly realizes the body is not his own.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines the tent interior: canvas walls, wooden pillars, sleeping platform, brass washbasin, oil lamp light. @Image 2 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1 and keeps the same face, topknot, beard and clothing throughout. He is alone in the tent, on the sleeping platform in the center; the brass washbasin stands on a low wooden stand to his right.

[Event Script]
Stage 1 - Waking: Opening state: Han Igyeom lies asleep under a thick padded blanket. A war drum sounds outside. He sits bolt upright, grabs his lower back out of habit and groans in Korean, {아이고.} End state: he freezes with his hand still on his lower back.
Stage 2 - No pain: He presses his lower back again, bends one knee and straightens it, and blinks in surprise. He says quietly in Korean, {안 아프네.} End state: he lowers his eyes to his own hands.
Stage 3 - The body: He turns his smooth young hands over, squeezes his own thick forearm, then pats his flat stomach, his eyes widening a little more each time. End state: he leans toward the washbasin.
Stage 4 - The face: Over his shoulder into the basin, the still water shows a bearded young face. He asks the reflection politely in Korean, {누구세요.} The reflection's lips move with his. Cut to a close-up of his stunned face; the clip ends holding on that face.

[Visual and Camera Treatment]
Stage 1 is a medium shot at eye level. Stages 2 and 3 slowly push in to a waist-up shot. Stage 4 cuts to an over-the-shoulder shot into the basin, then to a close-up of his face. Warm amber oil-lamp light from the left; cold blue dawn light through the open tent flap on the right.

[Audio]
<a slow war drum outside>, <cloth rustling>, <a soft splash of water>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Only Han Igyeom speaks.

[Maintain Consistency]
Keep Han Igyeom's face, topknot, beard and black cheollik with the leather vest identical throughout; keep the washbasin on his right and the lamp light from the left.
```

## 테이크 기록

| 테이크 | 파일 | job | 결과 |
|---|---|---|---|
| 1 | `renders/ep01/clip05a_take1.mp4` | `025d13f9-6976-49f4-8487-4e4da9d20ce5` | 얼굴·의상·배경 유지 양호. 4단계 구성 그대로 나옴. 대사 발음은 사람이 들어서 확인 필요 |

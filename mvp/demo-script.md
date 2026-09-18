# Demo Video Pack — Suraksha Parchi | Team CHANAKYA (30-sec + 2-min)
Contact: ayush4ru@gmail.com

## Files
- `mvp/index.html` — clickable MVP (open in Chrome, project on screen)
- `mvp/demo_video.mp4` — auto-built 30-sec explainer (generated, no shoot needed)
- `mvp/demo-script.md` — this file = shot list + voiceover

## 30-sec storyboard (for PPT slide 6 QR + WhatsApp submission)
| Sec | Visual | Voiceover (Hindi, slow) |
|0-5| logo.png + Team CHANAKYA | "Doctor ki parchi samajh nahi aati? Hum hain Team Chanakya." |
|5-10| sample-parchi.png zoom | "Crocin, Azithro — scribble me koi kya samjhe?" |
|10-15| journey.png SCAN→READ | "Photo lo. AI padhta hai — offline bhi, Hindi me bhi." |
|15-20| phone-timetable.png | "Subah-dopahar-raat timetable, pictogram ke saath." |
|20-25| architecture.png | "Duplicate dose par RED alert. Bhashini voice Bengali, Marathi me." |
|25-30| logo + ayush4ru@gmail.com | "Suraksha Parchi — Clear Parchi, Safe Patient." |

## 2-min live demo (LPU stage / recording with mvp/index.html)
1. (0:00) Hook + show real parchi print. 2. (0:20) Open index.html → Use sample → READ → conf 87%. 3. (0:50) SAMJHAO → disease + diet. 4. (1:10) Voice suno (hi→bn→mr toggle). 5. (1:30) Add Dolo → RED duplicate alert fires (crowd wow). 6. (1:50) Save to Sehat File + Delete (privacy). Close with pilot ask.
Record: Chrome fullscreen → Win+G Xbox bar → 1080p → mic Hindi. Keep phone speaker near mic for TTS.

## How to re-build mp4
`python mvp/build_video.py` → outputs mvp/demo_video.mp4 (1280x720, 30fps). Needs imageio-ffmpeg (installed).

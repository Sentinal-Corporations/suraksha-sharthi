import asyncio, os
import edge_tts

NARS = [
"Namaste! Kya aapne kabhi doctor ki parchi padhne mein struggle kiya hai? Bharat mein saath pratishat se zyada parche haathon se likhe jaate hain, English mein. Meri daadi ne ek baar do dawaiyaan kha li thi, kyunki parchi koi padh nahi paaya. Hum hain Team Chanakya, aur ye hai Suraksha Parchi. Clear parchi, safe patient.",
"Problem chhoti nahi hai. Aadhe se zyada mareez galat dose lete hain. Har saal ek lakh se zyada mautein dawai ki galtiyon se hoti hain. Aur antibiotics beech mein chhodne se drug resistance badhta hai. Gaon tak swasthya pahunchane wali dus lakh Asha workers ke paas iska koi tool nahi hai.",
"Dekhiye live demo. Hum ek asli messy parchi ka photo lete hain — Crocin aur Azithro. Offline reader pehle padhta hai, phir smart reader handwriting samajh kar eighty-seven percent confidence tak pahunchta hai. Jo shabd pakka na ho, wahan tap-to-confirm button aata hai — insaan hamesha final authority rehta hai.",
"Ab Rog Samjhao. AI dekhta hai Metformin aur high sugar report, aur paanchvi class ke shabdon mein samjhata hai — ye sugar ki dawai hai, khaane ke saath lo, roz walk karo. Hindi, Bengali, Marathi — teenon mein awaaz, aur suraj-baadal-chaand wale chitra, taaki anpadh user bhi time-table follow kar sake.",
"Aur ab crowd moment. Crocin ke saath Dolo add karo — dono Paracetamol brand hain. App turant RED duplicate alert deta hai — overdose se liver kharab hoga, doctor se poochho. Insulin ya TB jaisi high-risk dawaiyon par app andaza kabhi nahi lagata — sirf referral deta hai.",
"Parchi ke aage Suvidha section hai. Jan Aushadhi price check batata hai — branded ke muqable Kendra ka daam, Metformin paintalis rupaye ke bajaye chaudah rupaye. Ayushman Bharat paanch lakh ke cashless cover tak pahunchata hai. Aur one-zero-eight jaise helplines — ek tap par call.",
"Menu mein sab kuch hai — privacy policy, user agreement, support. Aapki tasveeren private rehti hain, delete ek tap par. Aur sabse badi baat — internet na ho, tab bhi app chalti hai. Gaon ke liye offline-first banaya gaya hai.",
"Andar kya hai? Hybrid OCR, teen bhashaon wali awaaz, unchaas dawaiyon ka verified database, baarah interaction rules — aur Needle-2, chaudah megabyte ka AI model jo phone mein hi chalta hai, facts invent kiye bina. Team Chanakya — Ayush Pandey build karte hain, Kaushal Rawat field testing. Aaj parchi, kal sau crore Bharatiyon ki Sehat File. Dhanyavaad!",
"Form bhi bahut simple hai — naam optional hai, phone sirf reminders ke liye. Bhasha chuno — Hindi, Bengali ya Marathi — aur lakshan likh do, jaise teen din se bukhar. Phir Read dabao. Neeche chips mein dawaiyaan dikhengi — galat ho to cross dabao, sahi ho to Main result mein Enter karo.",
"Neeche Helplines section hai — one-zero-eight ambulance, one-one-two emergency, one-zero-four health helpline, fourteen-triple-five Ayushman. Har number ke saath Call button — ek tap par phone lag jata hai. Ayushman card ke steps bhi oopar likhe hain.",
]
OUT = r"C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\mvp\audio2"

async def gen(i, text):
    await edge_tts.Communicate(text, "hi-IN-SwaraNeural", rate="-12%").save(f"{OUT}/h{i}.mp3")
    print("saved", i)

async def main():
    os.makedirs(OUT, exist_ok=True)
    for i, t in enumerate(NARS):
        await gen(i, t)

asyncio.run(main())

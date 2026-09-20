// UI strings: hi / bn / mr. Medical facts come from assets/data, never from here.
class Strings {
  static const langs = ['hi', 'bn', 'mr'];
  static const langName = {'hi': 'Hindi', 'bn': 'Bengali', 'mr': 'Marathi'};
  static const ttsLocale = {'hi': 'hi-IN', 'bn': 'bn-IN', 'mr': 'mr-IN'};
  static const diet = {
    'hi': 'Ubla paani, bahar ka khana avoid, 3 din bukhar to doctor.',
    'bn': 'Fotano jol, bairer khabar avoid.',
    'mr': 'Ukalalele pani, baheril talha.',
  };
  static String voice(String nm, String dz, String lang) => {
        'hi': 'Namaste $nm. Aapko $dz ke liye dawai mili hai. Subah 1 goli khane ke baad, 5 din course pura karein.',
        'bn': 'Nomoskar $nm. Apnar $dz er jonno osudh. Sokale 1 ta khabar pore.',
        'mr': 'Namaskar $nm. Tumhala $dz sathi aushadh. Sakali 1 goli jevnanantar.',
      }[lang]!;
  static const disc = {
    'hi': 'Ye jankari hai, salah nahi. Doubt ho to ASHA/doctor se poochhein. Emergency: 108.',
    'bn': 'Eti tothyo, poramorsho noy. ASHA/doctor ke jiggesh korun.',
    'mr': 'Hi mahiti ahe, salla nahi. ASHA/doctor na vichara.',
  };
  static const intros = {
    'hi': ['AI ne aapki parchi padh li hai — aasan bhasha me samjhaya:', 'Parchi taiyaar — AI se saral me janiye:', 'AI vishleshan taiyaar hai — dhyaan se padhein:'],
    'bn': ['AI apnar parchi poreche — sohoj bhashay:', 'Parchi toiri — AI theke janun:', 'AI bishleshon toiri:'],
    'mr': ['AI ne tumchi parchi vachli — sopya bhashet:', 'Parchi tayar — AI kadun samja:', 'AI vishleshan tayar aahe:'],
  };
  static const tips = {
    'hi': ['AI tip: dawai roz same time par lo.', 'AI tip: course beech me mat chhodo.', 'AI tip: dawai ke saath paani khoob piyo.'],
    'bn': ['AI tip: roj ekei somoye osudh khan.', 'AI tip: course majhpathe chharben na.', 'AI tip: osudher sathe porjapto jol khan.'],
    'mr': ['AI tip: darroj ekach veli aushadh ghya.', 'AI tip: course madhyat sodu naka.', 'AI tip: aushadhasobat bharpur pani pya.'],
  };
}

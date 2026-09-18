Add-Type -AssemblyName System.Speech
$base = "C:\Users\Admin\Downloads\bharat innovation 2.0\CHANAKYA_SurakshaParchi\mvp\audio"
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$s.SelectVoice("Microsoft Zira Desktop"); $s.Rate = -3
0..9 | ForEach-Object {
  $t = Get-Content -LiteralPath "$base\scene$_.txt" -Raw -Encoding UTF8
  $nar = ($t -split "`n" | Where-Object { $_ -match "^NAR=" } | Select-Object -First 1) -replace "^NAR=",""
  $s.SetOutputToWaveFile("$base\scene$_.wav"); $s.Speak($nar); $s.SetOutputToNull()
  $w = Get-Item -LiteralPath "$base\scene$_.wav"
  "scene$_ : " + [math]::Round($w.Length/1024) + "KB"
}
"tts-done"
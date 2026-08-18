<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TrueVoice Test Drive</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(140deg, #f5f9ff 0%, #e9f2ff 100%);
      min-height: 100vh;
      padding: 24px 16px 60px;
      color: #1e1e2f;
    }

    .container {
      max-width: 680px;
      margin: 0 auto;
    }

    h1 {
      font-size: 2rem;
      text-align: center;
      color: #0b3d91;
      margin-bottom: 8px;
    }

    .subtitle {
      text-align: center;
      color: #3a5a8c;
      margin-bottom: 26px;
      font-size: 1rem;
    }

    .card {
      background: white;
      border-radius: 20px;
      padding: 22px;
      margin-bottom: 22px;
      box-shadow: 0 8px 24px rgba(13, 53, 120, 0.10);
    }

    label, .label {
      font-weight: 600;
      color: #0a2e6e;
      margin-bottom: 8px;
      display: block;
    }

    textarea {
      width: 100%;
      min-height: 120px;
      border: 1.5px solid #b7cef5;
      border-radius: 14px;
      padding: 14px;
      font-size: 1rem;
      resize: vertical;
      background: #f8fbff;
    }

    textarea:focus {
      outline: none;
      border-color: #0b3d91;
      background: white;
    }

    .wer-box {
      background: #0b3d91;
      color: white;
      padding: 16px;
      border-radius: 16px;
      text-align: center;
      margin-top: 14px;
    }

    .wer-score {
      font-size: 2.4rem;
      font-weight: 800;
      color: #ffd966;
    }

    .wer-note {
      font-size: 0.9rem;
      margin-top: 8px;
      color: #d9e6ff;
    }

    .buttons {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      justify-content: center;
      margin: 18px 0;
    }

    button {
      flex: 1;
      min-width: 130px;
      padding: 16px 18px;
      border-radius: 60px;
      border: none;
      font-size: 1.1rem;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.1s ease;
    }

    button:active { transform: scale(0.96); }

    .record {
      background: #e63946;
      color: white;
    }

    .stop {
      background: #1d3557;
      color: white;
    }

    .history {
      margin-top: 18px;
    }

    .history-item {
      background: #f1f6ff;
      border-left: 5px solid #0b3d91;
      padding: 12px 14px;
      border-radius: 10px;
      margin-bottom: 10px;
      font-size: 0.95rem;
    }

    footer {
      text-align: center;
      margin-top: 30px;
      font-size: 0.95rem;
      color: #1e2f50;
    }

    footer span {
      color: #0b3d91;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎙️ TrueVoice</h1>
    <p class="subtitle">Try it. Speak naturally. See the difference.</p>

    <div class="card">
      <label>🎤 Record your voice</label>
      <div class="buttons">
        <button class="record" onclick="startRecording()">Start Recording</button>
        <button class="stop" onclick="stopRecording()">Stop Recording</button>
      </div>
    </div>

    <div class="card">
      <label for="textInput">📝 Please type or paste your English text now or after your recording.</label>
      <textarea id="textInput" placeholder="Type or paste your English text here..."></textarea>

      <div class="wer-box" id="werBox">
        <div class="label" style="color:white;">📊 Word Error Rate</div>
        <div class="wer-score" id="werScore">—</div>
        <div class="wer-note">The Word Error Rate (WER) score will be shown after 5 recordings.</div>
      </div>
    </div>

    <div class="card history">
      <label>🕘 Recent transcriptions</label>
      <div id="historyList">
        <p style="color:#666;">No recordings yet. Your last 10 transcriptions will appear here.</p>
      </div>
    </div>

    <footer>
      <p>Contact: <span>William@ClassiAIhk.com</span></p>
      <p>Powered by <span>Nvidia Build</span></p>
    </footer>
  </div>

  <script>
    let recordingCount = 0;
    let transcriptHistory = [];

    function startRecording() {
      document.getElementById("werScore").innerText = "Recording...";
    }

    function stopRecording() {
      recordingCount++;
      const textInput = document.getElementById("textInput").value.trim();
      const transcript = textInput || `Sample transcription ${recordingCount}`;

      transcriptHistory.unshift(transcript);
      if (transcriptHistory.length > 10) transcriptHistory.pop();

      renderHistory();

      if (recordingCount >= 5) {
        const sampleWer = (0.14 + Math.random() * 0.2).toFixed(2);
        document.getElementById("werScore").innerText = `${Math.round(sampleWer * 100)}%`;
      } else {
        document.getElementById("werScore").innerText = "—";
      }
    }

    function renderHistory() {
      const list = document.getElementById("historyList");
      list.innerHTML = "";
      transcriptHistory.forEach(item => {
        const div = document.createElement("div");
        div.className = "history-item";
        div.innerText = item;
        list.appendChild(div);
      });
    }
  </script>
</body>
</html>

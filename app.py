<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Classi AI | Universal Fluency Layer</title>
    <style>
        :root {
            --bg: #050816;
            --card: #0b1026;
            --accent: #4f7cff;
            --text: #f2f4ff;
            --muted: #aab3d0;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 60px 24px;
        }

        h1 {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 24px;
            background: linear-gradient(90deg, #ffffff, #8fa7ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .subhead {
            font-size: 1.25rem;
            color: var(--muted);
            margin-bottom: 48px;
            max-width: 900px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 24px;
            margin: 60px 0;
        }

        .card {
            background: var(--card);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 18px;
            padding: 24px;
            transition: transform 0.2s ease, border 0.2s ease;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: rgba(79,124,255,0.5);
        }

        .card h3 {
            margin-bottom: 12px;
            color: #fff;
        }

        .card p {
            color: var(--muted);
            font-size: 0.95rem;
        }

        .recording-section {
            background: linear-gradient(135deg, #0b1026 0%, #131a38 100%);
            border: 1px solid rgba(79,124,255,0.25);
            border-radius: 24px;
            padding: 40px;
            margin: 70px 0;
            text-align: center;
        }

        .record-btn {
            background: var(--accent);
            color: white;
            border: none;
            padding: 18px 40px;
            font-size: 1.1rem;
            font-weight: 700;
            border-radius: 100px;
            cursor: pointer;
            transition: background 0.2s ease, transform 0.1s ease;
            margin: 0 8px;
        }

        .record-btn:hover {
            background: #3f68e6;
        }

        .record-btn:active {
            transform: scale(0.97);
        }

        .stop-btn {
            background: #d64545;
        }

        .stop-btn:hover {
            background: #b93535;
        }

        .audio-player {
            margin-top: 30px;
            width: 100%;
            max-width: 500px;
        }

        .status {
            color: var(--muted);
            font-size: 0.9rem;
            min-height: 24px;
            margin-top: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Classi AI</h1>
        <p class="subhead">
            A deep-tech AI infrastructure company delivering a proprietary 
            <strong>Universal Fluency Layer</strong> for voice-to-text and LLM systems.
        </p>

        <div class="grid">
            <div class="card">
                <h3>Personalized Acoustic Engine</h3>
                <p>Adapts to each user's voice, accent, and environment without retraining large models.</p>
            </div>
            <div class="card">
                <h3>Mapping & Inference Engine</h3>
                <p>Corrects acoustic-phonetic distortions before transcription using advanced inference.</p>
            </div>
            <div class="card">
                <h3>Grammar & Structural Engine</h3>
                <p>Refines post-ASR text for grammar, coherence, and semantic integrity.</p>
            </div>
            <div class="card">
                <h3>Closed-Loop Correction</h3>
                <p>Iteratively aligns audio with corrected text to recover missing or low-confidence words.</p>
            </div>
        </div>

        <div class="recording-section">
            <h2>Try the Fluency Layer</h2>
            <p style="color: #aab3d0; margin-bottom: 24px;">
                Record a short English voice sample to test clarity and pronunciation-aware transcription.
            </p>

            <button id="recordBtn" class="record-btn">Start Recording</button>
            <button id="stopBtn" class="record-btn stop-btn" disabled>Stop</button>

            <div class="status" id="status">Ready to record.</div>

            <audio id="audioPlayback" class="audio-player" controls style="display: none;"></audio>
        </div>
    </div>

    <script>
        let mediaRecorder;
        let recordedChunks = [];
        const recordBtn = document.getElementById('recordBtn');
        const stopBtn = document.getElementById('stopBtn');
        const status = document.getElementById('status');
        const audioPlayback = document.getElementById('audioPlayback');

        async function startRecording() {
            recordedChunks = [];
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorder = new MediaRecorder(stream);

                mediaRecorder.ondataavailable = (event) => {
                    if (event.data.size > 0) {
                        recordedChunks.push(event.data);
                    }
                };

                mediaRecorder.onstop = () => {
                    const blob = new Blob(recordedChunks, { type: 'audio/webm' });
                    const url = URL.createObjectURL(blob);
                    audioPlayback.src = url;
                    audioPlayback.style.display = 'block';
                    status.textContent = 'Recording saved. You can play it back below.';
                };

                mediaRecorder.start();
                status.textContent = 'Recording...';
                recordBtn.disabled = true;
                stopBtn.disabled = false;
            } catch (err) {
                status.textContent = 'Microphone access denied or unavailable.';
                console.error(err);
            }
        }

        function stopRecording() {
            if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                mediaRecorder.stop();
                mediaRecorder.stream.getTracks().forEach(track => track.stop());
                recordBtn.disabled = false;
                stopBtn.disabled = true;
            }
        }

        recordBtn.addEventListener('click', startRecording);
        stopBtn.addEventListener('click', stopRecording);
    </script>
</body>
</html>

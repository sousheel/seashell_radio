from flask import Flask, render_template_string, Response


app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(
        """
            <html>
            <head>
                <title>Seashell Radio</title>
            </head>
            <body>
                <h1>Seashell Radio</h1>
                <hr />
                <a href="/play">http://localhost:69420/play</a>
                <a href="/mp3">http://localhost:69420/mp3</a>
            </body>
            </html>
        """
        )

@app.route("/mp3")
def streammp3():
    def generate():
        with open("signals/song.mp3", "rb") as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/mp3")


@app.route('/play')
def play():
    return Response(
            # frame_generator(),
            # mimetype='multipart/x-mixed-replace; boundary=frame'
        )

# def frame_generator():
#     while (True):
#         # Get Image
#         response_image = client.simGetImage(CAMERA_NAME, IMAGE_TYPE)
#         np_response_image = np.asarray(bytearray(response_image), dtype="uint8")
#         # Publish to ROS
#
#         # Decode Image
#         decoded_frame = cv2.imdecode(np_response_image, cv2.IMREAD_COLOR)
#         ret, encoded_jpeg = cv2.imencode(DECODE_EXTENSION, decoded_frame)
#         frame = encoded_jpeg.tobytes()
#         # Return Decoded Image
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=69420)

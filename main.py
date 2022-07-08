from datetime import datetime
import logging
import os

from flask import Flask, redirect, render_template, request

from google.cloud import storage


CLOUD_STORAGE_BUCKET = os.environ.get("CLOUD_STORAGE_BUCKET")


app = Flask(__name__)


@app.route("/")
def homepage():
    # get image from cloud storage name profile_picture.jpg
    fname = 'profile_image.jpg'

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)
    blob = bucket.blob(fname)

    image_url = blob.public_url

    return render_template("index.html", image_url=image_url)


@app.route("/upload_photo", methods=["GET", "POST"])
def upload_photo():
    if request.method == "POST":
        # check delete storage if blob exist
        # read upload photo
        fname = 'profile_image.jpg'
        photo = request.files["file"]

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)

        stats = storage.Blob(bucket=bucket, name=fname).exists(storage_client)
        
        if stats:
            _ = bucket.blob(fname).delete(storage_client)

        blob = bucket.blob(fname)
        blob.upload_from_string(photo.read(), content_type=photo.content_type)
        blob.make_public()

        return redirect("/")

    elif request.method == "GET":
        # render template for upload photo
        return render_template("upload.html")


@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return (
        """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(
            e
        ),
        500,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

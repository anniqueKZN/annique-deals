from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
  # Default fallback consultant reference ID if none provided in query params
  ref = request.args.get("ref", "527160")
  return render_template("index.html", ref=ref)


@app.route("/collections/<collection_name>")
def redirect_collection(collection_name):
  ref = request.args.get("ref", "527160")
  # Safely forward collection requests directly to Annique with tracking
  target_url = (
      f"https://www.annique.com/collections/{collection_name}?ref={ref}"
  )
  return redirect(target_url)


if __name__ == "__main__":
  app.run(debug=True, port=5000)

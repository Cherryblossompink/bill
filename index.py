from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Bill Calculator</title>
</head>
<body>

<h1>Bill Calculator</h1>

<form method="POST">
<label>Item name: </label>
<input type="text" name="item" required><br><br>

<label>Quantity: </label>
<input type="number" name="quantity" required><br><br>

<label>Price per Item: </label>
<input type="number" name="price" step="0.01" required><br><br>

<button type="submit">Calculate Bill</button>
</form>

{% if total is not none %}
<h2>Bill Summary<h2>
<p>Item: {{ item }}</p>
<p>Quantity: {{ quantity }}</p>
<p>Price: {{ price }}</p>
<h3>Total Bill: KSh {{ total }}</h3>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    total = None

    if request.method == "POST":
        item = request.form["item"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        total = quantity * price

        return render_template_string(
            html,
            item=item,
            quantity=quantity,
            price=price,
            total=total
        )

    return render_template_string(html, total=total)


if __name__ == "__main__":
    app.run(debug=True)    
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>St Thomas Public School</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{
    background:#f4f6f9;
    color:#222;
}

/* ================= NAVBAR ================= */
header{
    background:linear-gradient(90deg,#003366,#0059b3);
    padding:18px 40px;
    position:sticky;
    top:0;
    z-index:1000;
}

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

nav h1{
    color:white;
    font-size:26px;
    font-weight:600;
}

nav ul{
    list-style:none;
    display:flex;
    gap:25px;
}

nav ul li a{
    color:white;
    text-decoration:none;
    font-weight:400;
    transition:opacity 0.3s;
}

nav ul li a:hover{
    opacity:0.8;
}

/* ================= HERO ================= */
.hero{
    height:88vh;
    background:
        linear-gradient(
            rgba(0,40,90,0.75),
            rgba(0,40,90,0.75)
        ),
        url("/static/images/school_building.jpg");
    background-size:cover;
    background-position:center;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
}

.hero-box{
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(8px);
    padding:40px 70px;
    border-radius:18px;
    animation:fadeUp 1.2s ease;
}

.hero-box h2{
    color:white;
    font-size:44px;
    font-weight:600;
    letter-spacing:1px;
}

.hero-box p{
    color:#ffdd55;
    font-size:18px;
    margin-top:10px;
}

.hero-line{
    width:90px;
    height:4px;
    background:#ffcc00;
    margin:18px auto 0;
    border-radius:4px;
}

/* ================= SECTIONS ================= */
section{
    padding:80px 40px;
}

section h2{
    text-align:center;
    font-size:34px;
    color:#003366;
    margin-bottom:25px;
}

section p{
    max-width:900px;
    margin:auto;
    text-align:center;
    line-height:1.8;
    font-size:17px;
}

/* ================= FACILITIES ================= */
.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:30px;
    margin-top:40px;
}

.card{
    background:white;
    border-radius:16px;
    overflow:hidden;
    box-shadow:0 12px 30px rgba(0,0,0,0.12);
    transition:transform 0.35s;
}

.card:hover{
    transform:translateY(-10px);
}

.card img{
    width:100%;
    height:220px;
    object-fit:cover;
}

.card h3{
    padding:18px;
    text-align:center;
    font-size:20px;
}

/* ================= GALLERY ================= */
.gallery{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:25px;
    margin-top:40px;
}

.gallery img{
    width:100%;
    border-radius:16px;
    transition:transform 0.35s,box-shadow 0.35s;
}

.gallery img:hover{
    transform:scale(1.05);
    box-shadow:0 18px 40px rgba(0,0,0,0.2);
}

/* ================= CONTACT ================= */
.contact{
    max-width:600px;
    margin:auto;
    background:white;
    padding:40px;
    border-radius:18px;
    box-shadow:0 12px 30px rgba(0,0,0,0.15);
}

.contact input,
.contact textarea{
    width:100%;
    padding:14px;
    margin-bottom:15px;
    border-radius:10px;
    border:1px solid #ccc;
}

.contact button{
    width:100%;
    padding:14px;
    background:linear-gradient(90deg,#003366,#0059b3);
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    cursor:pointer;
}

/* ================= FOOTER ================= */
footer{
    background:#002244;
    color:white;
    text-align:center;
    padding:22px;
}

/* ================= ANIMATION ================= */
@keyframes fadeUp{
    from{opacity:0;transform:translateY(40px);}
    to{opacity:1;transform:translateY(0);}
}
</style>
</head>

<body>

<header>
<nav>
<h1>St Thomas Public School</h1>
<ul>
<li><a href="#home">Home</a></li>
<li><a href="#about">About</a></li>
<li><a href="#facilities">Facilities</a></li>
<li><a href="#gallery">Gallery</a></li>
<li><a href="#contact">Contact</a></li>
</ul>
</nav>
</header>

<div class="hero" id="home">
    <div class="hero-box">
        <h2>Education • Discipline • Excellence</h2>
        <p>“Education is Power”</p>
        <div class="hero-line"></div>
    </div>
</div>

<section id="about">
<h2>About Our School</h2>
<p>
St Thomas Public School is a value-based English medium institution dedicated to nurturing
young minds . Guided by our motto <strong>“Education is Power”</strong>,
we focus on academic excellence, discipline, moral values, and holistic development.
</p>
<br><br>
<p>
Our mission is to create a safe, supportive, and inspiring learning environment where
students develop confidence, responsibility, and lifelong learning skills. We believe that
education is not just about books, but about shaping character and preparing students
for the future.
</p>
</section>

<section id="facilities">
<h2>Our Facilities</h2>
<div class="cards">
<div class="card"><img src="/static/images/classroom.jpg"><h3>Classrooms</h3></div>
<div class="card"><img src="/static/images/library.jpg"><h3>Reading Area</h3></div>
<div class="card"><img src="/static/images/science_lab.jpg"><h3>Science Laboratory</h3></div>
<div class="card"><img src="/static/images/playground.jpg"><h3>PlayArea</h3></div>
</div>
</section>

<section id="gallery">
<h2>School Gallery</h2>

<div class="gallery">
    <img src="/static/images/school_building.jpg">
    <img src="/static/images/classroom.jpg">
    <img src="/static/images/library.jpg">
    <img src="/static/images/science_lab.jpg">
    <img src="/static/images/playground.jpg">

    <!-- NEW PHOTOS -->
    <img src="/static/images/gallery1.jpg">
    <img src="/static/images/gallery2.jpg">
    <img src="/static/images/gallery3.jpg">
    <img src="/static/images/gallery4.jpg">
    <img src="/static/images/gallery5.jpg">
</div>
</section>

<section id="contact">
<h2>Contact Us</h2>
<div class="contact-info">
    <p><strong>Phone:</strong> 9035763109, 8553051042</p>
    <p><strong>Email:</strong> st.thomaspublicschool@gmail.com</p>
    <p><strong>Address:</strong> St Thomas Public School, Krishnarajapuram, Kurudusonnenahalli, Bengaluru, Karnataka - 560067</p>
</div>

<div class="contact">
<form method="POST">
<input type="text" placeholder="Your Name" required>
<input type="email" placeholder="Your Email" required>
<textarea rows="5" placeholder="Your Message" required></textarea>
<button type="submit">Send Message</button>
</form>
</div>
</section>

<footer>
<p>© 2026 St Thomas Public School | Education is Power</p>
</footer>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

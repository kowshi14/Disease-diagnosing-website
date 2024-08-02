EssentialFat = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-U   A-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BodyFat</title>

    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i" rel="stylesheet">
    <link href="{{url_for('static', filename='main.css')}}" rel="stylesheet" media="all">
    
    <style>
        @import url('https://fonts.googleapis.com/css?family=Montserrat:500');
        *{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            background-color: #24252A;
        }
        li, a, button {
            font-family:"Montserrat", sans-serif;
            font-weight: 500;
            font-size: 16px;
            color: #edf0f1;
            text-decoration: none;
        }

        header{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 10%;
        }
        .nav_links{
            list-style: none;
        }
        .nav_links li{
            display: inline-block;
            padding: 0px 20px;
        }
        .nav_links li a{
            transition: all 0.3s ease 0s;
        }
        .nav_links li a:hover{
            color: #0088a9;
        }
        button{
            padding: 9px 25px;
            background-color: rgba(0,136,169,1);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease 0s;
        }
        button:hover{
            background-color: rgba(0,136,169,0.8);
        }
        .form-group{
            align-items: center;
            margin: 250px;
            margin-left: 800px;
            margin-top: 200px;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul class = "nav_links">
                <li>LOGO</li>
                <li><a href="/">Home</a></li>
                <li><a href="#">About Us</a></li>
            </ul>
        </nav>
        <a class = "cta" href="#"><button>Contact Us</button></a>
    </header>

    <h2 style="color: white">We have found that your Body Fat is {}%. So You come under Essential Fat Category You should take some more fat items</h2><br><br><br><br>
    <h3><a href="https://www.healthline.com/nutrition/why-you-gain-fat">Click here</a> to know how to get more Fat</h3>
</body>
</html>"""

Athletes = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BodyFat</title>

    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i" rel="stylesheet">
    <link href="{{url_for('static', filename='main.css')}}" rel="stylesheet" media="all">
    
    <style>
        @import url('https://fonts.googleapis.com/css?family=Montserrat:500');
        *{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            background-color: #24252A;
        }
        li, a, button {
            font-family:"Montserrat", sans-serif;
            font-weight: 500;
            font-size: 16px;
            color: #edf0f1;
            text-decoration: none;
        }

        header{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 10%;
        }
        .nav_links{
            list-style: none;
        }
        .nav_links li{
            display: inline-block;
            padding: 0px 20px;
        }
        .nav_links li a{
            transition: all 0.3s ease 0s;
        }
        .nav_links li a:hover{
            color: #0088a9;
        }
        button{
            padding: 9px 25px;
            background-color: rgba(0,136,169,1);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease 0s;
        }
        button:hover{
            background-color: rgba(0,136,169,0.8);
        }
        .form-group{
            align-items: center;
            margin: 250px;
            margin-left: 800px;
            margin-top: 200px;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul class = "nav_links">
                <li>LOGO</li>
                <li><a href="/">Home</a></li>
                <li><a href="#">About Us</a></li>
            </ul>
        </nav>
        <a class = "cta" href="#"><button>Contact Us</button></a>
    </header>

    <h2 style="color: white">We have found that your Body Fat is {}%. So You come under Athletes Fat Category You are Absolutely fit </h2><br><br><br><br>
</body>
</html>"""

Obese = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BodyFat</title>

    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i" rel="stylesheet">
    <link href="{{url_for('static', filename='main.css')}}" rel="stylesheet" media="all">
    
    <style>
        @import url('https://fonts.googleapis.com/css?family=Montserrat:500');
        *{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            background-color: #24252A;
        }
        li, a, button {
            font-family:"Montserrat", sans-serif;
            font-weight: 500;
            font-size: 16px;
            color: #edf0f1;
            text-decoration: none;
        }

        header{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 10%;
        }
        .nav_links{
            list-style: none;
        }
        .nav_links li{
            display: inline-block;
            padding: 0px 20px;
        }
        .nav_links li a{
            transition: all 0.3s ease 0s;
        }
        .nav_links li a:hover{
            color: #0088a9;
        }
        button{
            padding: 9px 25px;
            background-color: rgba(0,136,169,1);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease 0s;
        }
        button:hover{
            background-color: rgba(0,136,169,0.8);
        }
        .form-group{
            align-items: center;
            margin: 250px;
            margin-left: 800px;
            margin-top: 200px;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul class = "nav_links">
                <li>LOGO</li>
                <li><a href="/">Home</a></li>
                <li><a href="#">About Us</a></li>
            </ul>
        </nav>
        <a class = "cta" href="#"><button>Contact Us</button></a>
    </header>

    <h2 style="color: white">We have found that your Body Fat is {}%. So You come under Obese Fat Category You should Burn up your fat in your body</h2><br><br><br><br>
    <h3><a href="https://www.healthline.com/nutrition/best-ways-to-burn-fat">Click here</a> to know how to get more Fat</h3>
</body>
</html>"""
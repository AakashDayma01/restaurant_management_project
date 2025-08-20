<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset='UTF-8'>
    <title>Restaurant Menu</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            background: #fafafa;
            margin: 0;
            padding: 0;
        }
        header{
            background: #ff6f61;
            padding: 20px;
            text-align: center;
            color: white;
        }
        h1{
            margin: 0;
        }
        .menu-container{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap:15px;
            padding: 20px;
        }
        .menu-item{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        }
        .menu-item h3{
            margin: 0 0 10px;
        }
        .price{
            color: #ff6f61;
            font-weigth:bold;
        }
    </style>
    </head>
    <body>
        <header>
        <h1>Our Restaurant Menu</h1>
        </header>

    <div class='menu-container'>
        {% for item in menu_items %}
        <div class='menu-item'>
        <h3>{{item.name}}</h3>
        <p>{{item.description}}</p>
        <p class='price'>{{item.price}}</p>

        </div>

        {% empty %}
        <p> No menu items available. </p>
        {% endfor %}

    </div>
</body>
</html>
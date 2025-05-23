
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Image Downloader</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        h1 {
            color: #4CAF50;
            font-size: 2.5em;
        }

        form {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            display: flex;
            flex-direction: column;
        }

        label {
            margin-top: 10px;
            font-weight: bold;
        }

        input[type="text"],
        input[type="number"] {
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 100%;
            font-size: 1em;
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.1em;
        }

        button:hover {
            background-color: #45a049;
        }

        @media (max-width: 600px) {
            form {
                width: 100%;
                padding: 15px;
            }

            h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div>
        <h1>Google Image Downloader</h1>
        <form action="/search" method="POST">
            <label for="query">Search Query:</label>
            <input type="text" id="query" name="query" placeholder="Enter search term" required>
            <label for="number">Number of Images:</label>
            <input type="number" id="number" name="number" min="1" max="10" placeholder="1-10" required>
            <button type="submit">Download Images</button>
        </form>
    </div>
</body>
</html>
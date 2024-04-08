const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const port = 8080;

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('login.html');
});

app.post('/auth', (req, res) => {
  const u = req.body.username;
  const p = req.body.password;

  const db = new sqlite3.Database('l3.db');
  db.get(
    'SELECT * FROM creds WHERE username = ? AND password = ?',
    [u, p],
    (err, row) => {
      if (row) {
        res.render('landing.html');
      } else {
        res.send('Invalid credentials');
      }
    }
  );
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});


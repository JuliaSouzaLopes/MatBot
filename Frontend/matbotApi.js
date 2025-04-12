

const express = require('express');
const app = express();
const port = 8080;

app.use(express.json());

app.get('/', (req, res) => {
    res.send('API RESTful funcionando!');
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});


let usuarios = [];

app.get('/matbot', (req, res) => {
    res.json(usuarios);
});

app.post('/matbot', (req, res) => {
    const usuario = req.body;
    usuarios.push(usuario);
    res.status(201).json(usuario);
});



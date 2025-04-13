const { spawn } = require('child_process');
const bodyParser = require('body-parser')
const express = require('express')
const app = express()
const port = 3000


app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', (req, res) => {
  res.json({message: 'Hello World!'})
})

app.post('/enviaMensagem', async (req, res) => {

    //Validação dos dados do usuário
    const dadosUsuario = req.body;

    const processamentoBot = await botAPI(dadosUsuario);

    res.json({resultado: processamentoBot})
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

async function botAPI(dadosUsuario) {

    //TODO - Testar uma forma de o NOde executar o códico python do nosso chatbot
    const pythonProcess = spawn('python', ['chatbot.py', dadosUsuario.Mensagem]);

    pythonProcess.stdout.on('data',function(chunk){

        var textChunk = chunk.toString('utf8');// buffer to string
    
        return textChunk
    });

    return 'Xiiiiiiiii'
}
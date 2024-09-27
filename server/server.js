const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();
const {saveUser,fetchUser} = require('./userModel')
const app = express();

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Could not connect to MongoDB:', err));
// Define routes
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

app.post('/createUser', (req,res) =>{
    const userData = req.body
    saveUser(userData)
    res.send(userData)
})

app.get('/getUser', async (req,res) =>{
    const userId = req.query.userId
    console.log(userId)
    res.send(await fetchUser(userId))
})

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

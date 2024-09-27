// userModel.js

const mongoose = require('mongoose');

// Define the user schema
const userSchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true,
    unique: true, // Make userId unique
  },
  password: {
    type: String,
    required: true,
  },
  key: {
    type: String,
    required: true,
  },
});

// Create the User model
const User = mongoose.model('User', userSchema);

// Function to save a new user
const saveUser = async (userData) => {
  const user = new User(userData);
  try {
    await user.save();
    console.log('User saved successfully:', user);
  } catch (err) {
    console.error('Error saving user:', err);
    throw err;
  }
};

// Function to fetch a user by userId
const fetchUser = async (userId) => {
  try {
    const user = await User.findOne({ userId });
    if (user) {
      console.log('User fetched successfully:', user);
      return user;
    } else {
      console.log('User not found');
      return null;
    }
  } catch (err) {
    console.error('Error fetching user:', err);
    throw err;
  }
};

module.exports = { saveUser, fetchUser };

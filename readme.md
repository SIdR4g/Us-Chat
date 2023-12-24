
# Us-chat

Us-chat is a real-time chat website built using Django, leveraging WebSocket technology for smooth and instant messaging. Users can create and join rooms to engage in conversations with other participants. All messages from the conversations are saved, providing a persistent chat history.

## Features

- Real-time messaging using WebSocket
- Room creation and joining
- Persistent chat history
- Robust authentication

## Technologies Used

- Django
- Channels (for WebSocket support)
- Redis (for message caching)
- HTML, CSS, JavaScript (for the frontend)
  

## Getting Started

To run the Us-chat application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Us-chat.git
   cd Us-chat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and visit `http://localhost:8000` to access the Us-chat application.

## Usage

1. Open the Us-chat website.
2. Create a new account or log in.
3. Create or join a room.
4. Start chatting with other participants in real-time.

## Contributing

If you'd like to contribute to Us-chat, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or issues, please contact [your-email@example.com].

## Acknowledgments

- Mention any third-party libraries or resources used and give credit.


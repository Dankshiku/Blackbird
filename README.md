###                      Shikharsingh
Shikharsingh is basically an HTTP Denial of Service attack that affects threaded servers. It works like this:

We start making lots of HTTP requests.
We send headers periodically (every ~15 seconds) to keep the connections open.
We never close the connection unless the server does so. If the server closes a connection, we create a new one keep doing the same thing.
This exhausts the servers thread pool and the server can't reply to other people.

### INSTALLATION 
 • git clone https://github.com/Dankshiku/Shikharsingh

 • cd Shikharsinghhhh


 • python shikharsingh.py
<!--
**Shikharsinghhhh/Shikharsinghhhh** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

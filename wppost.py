from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost

your_blog = Client('http://192.81.215.238/xmlrpc.php', 'bangnidd', 'ok')

myposts=your_blog.call(posts.GetPosts())

post = WordPressPost()
post.title = 'MY_POST_TITLE'
post.slug='MY_POST_PERMANENT_LINK'
post.content = 'YOUR_POST_CONTENT'
post.id = your_blog.call(posts.NewPost(post))
post.post_status = 'publish'
your_blog.call(posts.EditPost(post.id, post))

import Get_blog_img
import Get_blog_id
blog_urls=Get_blog_id.Get_blog_id()
for blog_url in blog_urls:
    Get_blog_img.Get_blog_img(blog_url)
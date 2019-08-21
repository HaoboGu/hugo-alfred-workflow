# hugo-alfred-workflow
Alfred workflow for Hugo, a static site generator. 

This workflow provides shortkey for markdown document to hugo post migration, creating new hugo post and one-click deploy.

## Usage

If you do not know hugo, please check https://gohugo.io/getting-started/.

### Set hugo source folder

First you should set your hugo source folder using `hugoset`:

![image-20190821210929425](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-130929.png)

This command will set this folder's path in environment variables. 

If your source folder is changed, you must set it again.

### Markdown document migration

If you want to migrate your markdown docs to hugo posts, use `hgtran`:

![image-20190821211256084](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-131256.png)

Then this file will be copied to `hugo-source-folder/content/posts/` and a simple [hugo front matter](https://gohugo.io/content-management/front-matter/) will be added to the head of the post file. The post file will be automatically opened for you:

![image-20190821211654105](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-131654.png)

### Create new hugo post

You can create new hugo post using `hgnew`:

![image-20190821211811136](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-131811.png)

Note that you **CANNOT** use filenames with whitespaces.

Similarly, the created file will be opened automatically with a simple hugo front matter:

![image-20190821212024203](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-132024.png)

### Deploy

Before deploy your site, make sure you have `deploy.sh` in your hugo source folder and you can deploy your site using `./deploy.sh` in the root of your hugo source folder. Please check [hugo's official doc](https://gohugo.io/hosting-and-deployment/hosting-on-github/) first.

Use `deploy` in Alfred to deploy your site:

![image-20190821212321837](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-132322.png)

The Alfred will automatically open the terminal and run the deploy script:

![image-20190821212432042](http://haobo-markdown.oss-cn-zhangjiakou.aliyuncs.com/markdown/2019-08-21-132432.png)

## Contribution

This workflow is in a very early stage, any kinds of contribution are welcome! 
Please feel free to open an issue if you have any questions or suggestions!



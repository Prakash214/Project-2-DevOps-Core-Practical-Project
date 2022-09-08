 create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

Service #1
The core service – this will render the Jinja2 templates and need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

Service #2 + #3
These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.

Service #4
This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.

The requirements of the project are as follows:

This could also provide a record of any issues or risks that you faced creating your project.

risk assessmenet
![image](https://i.gyazo.com/d0f7d7f9f2596fc63a0485ab1f2c1fdf.png)



An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.

trello board
![image](https://i.gyazo.com/fd61d17ffe5171bd2642e40289bc6c1e.png)

An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
gcp
![image](https://i.gyazo.com/c7ad92361bbb5d3429ee4bb28fa1863f.png)
app
![image](https://i.gyazo.com/e66b33cb5c8233a5ce30eb182ebd2b50.png)
![image](https://i.gyazo.com/98df5763b98c90ea59e5f9271f76b69f.png)
![image](https://i.gyazo.com/55f075fa444e020866370fff89f3fc96.png)

If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
webhook

![image](https://i.gyazo.com/603f950abf2ea1698c67988178e32a26.png)

jenkins pipeline
![image](https://i.gyazo.com/cb33aed31a5293e25486c6c871f54586.png)


The project must be deployed using containerisation and an orchestration tool.
docker-compose containerisation
![image](https://i.gyazo.com/79bf91eeba4cd8abf89548c3a3872837.png)


mock test shows 100% coverage and working in csv and pipeline
![image](https://i.gyazo.com/459a185da134b4b2cca4b3342b4966ce.png)
![image](https://i.gyazo.com/32e18e8c80a868b3195b21481ed4187c.png)
![image](https://i.gyazo.com/8133f9b8446d4863f3857061c1f42ff4.png)
![image](https://i.gyazo.com/7dd33e2518636a5457dbbfb68f33a2e8.png)
![iamge](https://i.gyazo.com/1fffa9439f458153fdf82a0b6c21d39e.png)

The project must make use of a reverse proxy to make your application accessible to the user.
![image](https://i.gyazo.com/8481a069bc231157e599d8448f3b52f8.png)

TO DO:
As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
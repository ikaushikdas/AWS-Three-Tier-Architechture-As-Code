from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("AWS Three Tier Architecture", show=False):
    with Cluster("Presentation Layer"):
        user_interface = EC2("Web Server\n(User Interface)")
        load_balancer = ELB("Load Balancer")
    
    with Cluster("Application Layer"):
        app_server = EC2("App Server\n(Business Logic)")
    
    with Cluster("Data Storage Layer"):
        database = RDS("Database\n(SQL, NoSQL)")
    
    user_interface >> load_balancer >> app_server >> database
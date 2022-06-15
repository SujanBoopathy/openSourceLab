#include<QApplication>
#include<QPushButton>

int main(int argc,char *argv[]){
    QApplication app(argc,argv);
    QPushButton helloButton("hello world");
    helloButton.resize(10,8);
    helloButton.show()
    return app.exec()
}
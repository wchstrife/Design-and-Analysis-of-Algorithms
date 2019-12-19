#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    bf = new BruteForce ();
    kmp = new KMP();
    bm = new BoyerMoore();

    connect(bf, SIGNAL(returnPreTime(double)), this, SLOT(setPreLabel(double)));
    connect(bf, SIGNAL(returnMatchTime(double)), this, SLOT(setMatchLabel(double)));
    connect(bf, SIGNAL(returnTotalTime(double)), this, SLOT(setTotalLabel(double)));
    connect(bf, SIGNAL(returnResults(QString)), this, SLOT(setResults(QString)));

    connect(kmp, SIGNAL(returnPreTime(double)), this, SLOT(setPreLabel(double)));
    connect(kmp, SIGNAL(returnMatchTime(double)), this, SLOT(setMatchLabel(double)));
    connect(kmp, SIGNAL(returnTotalTime(double)), this, SLOT(setTotalLabel(double)));
    connect(kmp, SIGNAL(returnResults(QString)), this, SLOT(setResults(QString)));

    connect(bm, SIGNAL(returnPreTime(double)), this, SLOT(setPreLabel(double)));
    connect(bm, SIGNAL(returnMatchTime(double)), this, SLOT(setMatchLabel(double)));
    connect(bm, SIGNAL(returnTotalTime(double)), this, SLOT(setTotalLabel(double)));
    connect(bm, SIGNAL(returnResults(QString)), this, SLOT(setResults(QString)));
}

MainWindow::~MainWindow()
{
    delete bf;
    delete kmp;
    delete bm;
    delete ui;
}

// 输入文件
void MainWindow::on_pushButton_T_clicked(bool checked)
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Select Text File"), filePath, tr("Allfile(*.*);;txtfile(*.txt)"));
    if (fileName != "")
        ui->lineEdit_T->setText(fileName);
    filePath = fileName.mid(0, fileName.lastIndexOf('/'));
}

void MainWindow::on_pushButton_P_clicked(bool checked)
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Select Text File"), filePath, tr("Allfile(*.*);;txtfile(*.txt)"));
    if (fileName != "")
        ui->lineEdit_P->setText(fileName);
    filePath = fileName.mid(0, fileName.lastIndexOf('/'));
}

// 执行算法
void MainWindow::on_pushButton_run_clicked(bool checked)
{
    t = "";
    p = "";

    if(matching){
        QMessageBox::warning(this, "Error!", "Matching!");
        return;
    }

    resetLabels();

    // 读取匹配串T
    QFile fileT(ui->lineEdit_T->text());

    if (!fileT.open(QIODevice::ReadOnly|QIODevice::Text))
    {
        QMessageBox::warning(this, "Error!", "读取文本T失败！");
        return;
    }

    QTextStream txtInputT(&fileT);
    while (!txtInputT.atEnd())
        t += txtInputT.readLine();
    fileT.close();

    // 读取模式串P
    QFile fileP(ui->lineEdit_P->text());

    if (!fileP.open(QIODevice::ReadOnly|QIODevice::Text))
    {
        QMessageBox::warning(this, "Error!", "读取文本P失败！");
        return;
    }

    QTextStream txtInputP(&fileP);
    while (!txtInputP.atEnd())
        p += txtInputP.readLine();
    fileP.close();

    // 统计输入字符数量
    int t_length = t.length();
    int p_length = p.length();
    ui->tLengthLabel->setText(QString::number(t_length));
    ui->pLengthLabel->setText(QString::number(p_length));

    if (t_length == 0){
        QMessageBox::warning(this, "Error!", "文本T不能为空字符串！");
        return;
    }

    if (p_length == 0){
        QMessageBox::warning(this, "Error!", "模式P不能为空字符串！");
        return;
    }

    if (t_length < p_length){
        QMessageBox::warning(this, "Error!", "文本T长度小于模式P长度！");
        return;
    }

    bfMatching = true;
    matching = true;
    bf->setAttr(p, t);
    bf->start();

}

// 清除所有label的信息
void MainWindow::resetLabels(){
    ui->bfPreLabel->clear();
    ui->bfMatchLabel->clear();
    ui->bfTotalLabel->clear();
    ui->bfResultLabel->clear();

    ui->kmpPreLabel->clear();
    ui->kmpMatchLabel->clear();
    ui->kmpTotalLabel->clear();
    ui->kmpResultLabel->clear();

    ui->bmPreLabel->clear();
    ui->bmMatchLabel->clear();
    ui->bmTotalLabel->clear();
    ui->bmResultLabel->clear();
}

void MainWindow::setPreLabel(double time)
{
    if (bfMatching){
        ui->bfPreLabel->setText(QString::number(time) + "s");
    }
    else if(kmpMathcing){
        ui->kmpPreLabel->setText(QString::number(time) + "s");
    }
    else if(bmMathcing){
        ui->bmPreLabel->setText(QString::number(time) + "s");
    }
}

void MainWindow::setMatchLabel(double time)
{
    if (bfMatching){
        ui->bfMatchLabel->setText(QString::number(time) + "s");
    }
    else if(kmpMathcing){
        ui->kmpMatchLabel->setText(QString::number(time) + "s");
    }
    else if(bmMathcing){
        ui->bmMatchLabel->setText(QString::number(time) + "s");
    }
}


void MainWindow::setTotalLabel(double time)
{
    if (bfMatching){
        ui->bfTotalLabel->setText(QString::number(time) + "s");
    }
    else if(kmpMathcing){
        ui->kmpTotalLabel->setText(QString::number(time) + "s");
    }
    else if(bmMathcing){
        ui->bmTotalLabel->setText(QString::number(time) + "s");
    }
}

void MainWindow::setResults(QString result)
{
    if (result == ""){
        result = "在文本T中未找到模式串P";
    }

    if (bfMatching){
        ui->bfResultLabel->setText(result);
        bfMatching = false;
        kmpMathcing = true;
        kmp->setAttr(p, t);
        kmp->start();
    }
    else if(kmpMathcing){
        ui->kmpResultLabel->setText(result);
        kmpMathcing = false;
        bmMathcing = true;
        bm->setAttr(p, t);
        bm->start();
    }
    else if(bmMathcing){
        ui->bmResultLabel->setText(result);
        matching = false;
        bmMathcing = false;
    }
}

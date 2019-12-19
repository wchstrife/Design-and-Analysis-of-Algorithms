#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>
#include <QFileDialog>
#include <QFile>
#include <QTextStream>

#include "brute-force.h"
#include "boyermoore.h"
#include "kmp.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_T_clicked(bool checked);

    void on_pushButton_P_clicked(bool checked);

    void on_pushButton_run_clicked(bool checked);

    void setPreLabel(double);

    void setMatchLabel(double);

    void setTotalLabel(double);

    void setResults(QString);

private:
    Ui::MainWindow *ui;

    QString p, t;

    QString filePath = "C:/";

    bool bfMatching = false, kmpMathcing = false, bmMathcing = false, matching = false;

    BruteForce *bf;

    KMP *kmp;

    BoyerMoore *bm;

    void resetLabels();     //清除所有的label
};

#endif // MAINWINDOW_H

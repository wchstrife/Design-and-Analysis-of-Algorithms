/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *label;
    QLineEdit *lineEdit_T;
    QLabel *label_2;
    QLineEdit *lineEdit_P;
    QPushButton *pushButton_T;
    QPushButton *pushButton_P;
    QPushButton *pushButton_run;
    QLabel *label_4;
    QLabel *label_11;
    QLabel *label_3;
    QLabel *kmpTotalLabel;
    QLabel *label_5;
    QLabel *kmpMatchLabel;
    QLabel *bfMatchLabel;
    QLabel *label_6;
    QLabel *bmResultLabel;
    QLabel *label_7;
    QLabel *bmTotalLabel;
    QLabel *label_9;
    QLabel *bmPreLabel;
    QLabel *label_8;
    QLabel *tLengthLabel;
    QLabel *kmpPreLabel;
    QLabel *bfPreLabel;
    QLabel *pLengthLabel;
    QLabel *label_10;
    QLabel *kmpResultLabel;
    QLabel *label_12;
    QLabel *bfResultLabel;
    QLabel *bmMatchLabel;
    QLabel *bfTotalLabel;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1077, 632);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(170, 30, 181, 31));
        QFont font;
        font.setFamily(QString::fromUtf8("Adobe Devanagari"));
        font.setPointSize(14);
        label->setFont(font);
        lineEdit_T = new QLineEdit(centralWidget);
        lineEdit_T->setObjectName(QString::fromUtf8("lineEdit_T"));
        lineEdit_T->setGeometry(QRect(170, 70, 561, 31));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(170, 120, 181, 31));
        label_2->setFont(font);
        lineEdit_P = new QLineEdit(centralWidget);
        lineEdit_P->setObjectName(QString::fromUtf8("lineEdit_P"));
        lineEdit_P->setGeometry(QRect(170, 160, 561, 31));
        pushButton_T = new QPushButton(centralWidget);
        pushButton_T->setObjectName(QString::fromUtf8("pushButton_T"));
        pushButton_T->setGeometry(QRect(770, 70, 75, 23));
        pushButton_P = new QPushButton(centralWidget);
        pushButton_P->setObjectName(QString::fromUtf8("pushButton_P"));
        pushButton_P->setGeometry(QRect(770, 160, 75, 23));
        pushButton_run = new QPushButton(centralWidget);
        pushButton_run->setObjectName(QString::fromUtf8("pushButton_run"));
        pushButton_run->setGeometry(QRect(460, 210, 75, 23));
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(210, 340, 91, 41));
        QFont font1;
        font1.setPointSize(12);
        label_4->setFont(font1);
        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(90, 340, 101, 41));
        label_11->setFont(font1);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(100, 470, 41, 41));
        label_3->setFont(font1);
        kmpTotalLabel = new QLabel(centralWidget);
        kmpTotalLabel->setObjectName(QString::fromUtf8("kmpTotalLabel"));
        kmpTotalLabel->setGeometry(QRect(450, 420, 91, 41));
        kmpTotalLabel->setFont(font1);
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(100, 390, 41, 41));
        label_5->setFont(font1);
        kmpMatchLabel = new QLabel(centralWidget);
        kmpMatchLabel->setObjectName(QString::fromUtf8("kmpMatchLabel"));
        kmpMatchLabel->setGeometry(QRect(330, 420, 91, 41));
        kmpMatchLabel->setFont(font1);
        bfMatchLabel = new QLabel(centralWidget);
        bfMatchLabel->setObjectName(QString::fromUtf8("bfMatchLabel"));
        bfMatchLabel->setGeometry(QRect(330, 380, 91, 41));
        bfMatchLabel->setFont(font1);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(330, 340, 71, 41));
        label_6->setFont(font1);
        bmResultLabel = new QLabel(centralWidget);
        bmResultLabel->setObjectName(QString::fromUtf8("bmResultLabel"));
        bmResultLabel->setGeometry(QRect(570, 460, 261, 41));
        bmResultLabel->setFont(font1);
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(100, 430, 41, 41));
        QFont font2;
        font2.setPointSize(12);
        font2.setBold(false);
        font2.setWeight(50);
        label_7->setFont(font2);
        label_7->setLayoutDirection(Qt::LeftToRight);
        bmTotalLabel = new QLabel(centralWidget);
        bmTotalLabel->setObjectName(QString::fromUtf8("bmTotalLabel"));
        bmTotalLabel->setGeometry(QRect(450, 460, 91, 41));
        bmTotalLabel->setFont(font1);
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(370, 290, 91, 41));
        label_9->setFont(font1);
        bmPreLabel = new QLabel(centralWidget);
        bmPreLabel->setObjectName(QString::fromUtf8("bmPreLabel"));
        bmPreLabel->setGeometry(QRect(210, 460, 91, 41));
        bmPreLabel->setFont(font1);
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(450, 340, 81, 41));
        label_8->setFont(font1);
        tLengthLabel = new QLabel(centralWidget);
        tLengthLabel->setObjectName(QString::fromUtf8("tLengthLabel"));
        tLengthLabel->setGeometry(QRect(240, 290, 91, 41));
        tLengthLabel->setFont(font1);
        kmpPreLabel = new QLabel(centralWidget);
        kmpPreLabel->setObjectName(QString::fromUtf8("kmpPreLabel"));
        kmpPreLabel->setGeometry(QRect(210, 420, 91, 41));
        kmpPreLabel->setFont(font1);
        bfPreLabel = new QLabel(centralWidget);
        bfPreLabel->setObjectName(QString::fromUtf8("bfPreLabel"));
        bfPreLabel->setGeometry(QRect(210, 380, 91, 41));
        bfPreLabel->setFont(font1);
        pLengthLabel = new QLabel(centralWidget);
        pLengthLabel->setObjectName(QString::fromUtf8("pLengthLabel"));
        pLengthLabel->setGeometry(QRect(460, 290, 91, 41));
        pLengthLabel->setFont(font1);
        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(570, 340, 71, 41));
        label_10->setFont(font1);
        kmpResultLabel = new QLabel(centralWidget);
        kmpResultLabel->setObjectName(QString::fromUtf8("kmpResultLabel"));
        kmpResultLabel->setGeometry(QRect(570, 420, 261, 41));
        kmpResultLabel->setFont(font1);
        label_12 = new QLabel(centralWidget);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(150, 290, 91, 41));
        label_12->setFont(font1);
        bfResultLabel = new QLabel(centralWidget);
        bfResultLabel->setObjectName(QString::fromUtf8("bfResultLabel"));
        bfResultLabel->setGeometry(QRect(570, 380, 261, 41));
        bfResultLabel->setFont(font1);
        bmMatchLabel = new QLabel(centralWidget);
        bmMatchLabel->setObjectName(QString::fromUtf8("bmMatchLabel"));
        bmMatchLabel->setGeometry(QRect(330, 460, 91, 41));
        bmMatchLabel->setFont(font1);
        bfTotalLabel = new QLabel(centralWidget);
        bfTotalLabel->setObjectName(QString::fromUtf8("bfTotalLabel"));
        bfTotalLabel->setGeometry(QRect(450, 380, 91, 41));
        bfTotalLabel->setFont(font1);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1077, 23));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QApplication::translate("MainWindow", "\350\276\223\345\205\245\346\226\207\346\234\254T\357\274\232", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "\350\276\223\345\205\245\346\250\241\345\274\217P\357\274\232", nullptr));
        pushButton_T->setText(QApplication::translate("MainWindow", "\346\211\223\345\274\200txt\346\226\207\344\273\266", nullptr));
        pushButton_P->setText(QApplication::translate("MainWindow", "\346\211\223\345\274\200txt\346\226\207\344\273\266", nullptr));
        pushButton_run->setText(QApplication::translate("MainWindow", "\350\277\220\350\241\214\347\256\227\346\263\225", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "\351\242\204\345\244\204\347\220\206\346\227\266\351\227\264", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "\347\256\227\346\263\225\345\220\215\347\247\260", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "BM", nullptr));
        kmpTotalLabel->setText(QString());
        label_5->setText(QApplication::translate("MainWindow", "BF", nullptr));
        kmpMatchLabel->setText(QString());
        bfMatchLabel->setText(QString());
        label_6->setText(QApplication::translate("MainWindow", "\345\214\271\351\205\215\346\227\266\351\227\264", nullptr));
        bmResultLabel->setText(QString());
        label_7->setText(QApplication::translate("MainWindow", "KMP", nullptr));
        bmTotalLabel->setText(QString());
        label_9->setText(QApplication::translate("MainWindow", "\346\250\241\345\274\217P\351\225\277\345\272\246\357\274\232", nullptr));
        bmPreLabel->setText(QString());
        label_8->setText(QApplication::translate("MainWindow", "\346\200\273\350\277\220\350\241\214\346\227\266\351\227\264", nullptr));
        tLengthLabel->setText(QString());
        kmpPreLabel->setText(QString());
        bfPreLabel->setText(QString());
        pLengthLabel->setText(QString());
        label_10->setText(QApplication::translate("MainWindow", "\345\214\271\351\205\215\344\275\215\347\275\256", nullptr));
        kmpResultLabel->setText(QString());
        label_12->setText(QApplication::translate("MainWindow", "\346\226\207\346\234\254T\351\225\277\345\272\246\357\274\232", nullptr));
        bfResultLabel->setText(QString());
        bmMatchLabel->setText(QString());
        bfTotalLabel->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

#ifndef BOYERMOORE_H
#define BOYERMOORE_H

#include <QThread>
#include <QString>
#include <chrono>

using namespace std;
using namespace chrono;

class BoyerMoore : public QThread
{
    Q_OBJECT

public:
    BoyerMoore();
    ~BoyerMoore();

    void setAttr(QString p, QString t);

signals:
    void returnPreTime(double);
    void returnMatchTime(double);
    void returnTotalTime(double);
    void returnResults(QString);

protected:
    void run();

private:
    QString t, p;
    int bmBc[150];
    int Osuff[2000005];
    int bmGs[2000005];
    void computeBMBC(int m);
    void computeBMGS(int m);
    void computeOsuff(int m);
};

#endif // BOYERMOORE_H

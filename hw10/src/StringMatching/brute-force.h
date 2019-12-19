#ifndef BRUTEFORCE_H
#define BRUTEFORCE_H

#include <QThread>
#include <QString>
#include <chrono>

using namespace std;
using namespace chrono;

class BruteForce : public QThread
{
    Q_OBJECT

public:
    BruteForce();
    ~BruteForce();

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
};

#endif // BRUTEFORCE_H

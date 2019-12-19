#ifndef KMP_H
#define KMP_H
#include <QThread>
#include <QString>
#include <chrono>

using namespace std;
using namespace chrono;

class KMP :public QThread
{
    Q_OBJECT

public:
    KMP();
    ~KMP();
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
    int pre[2000005];
    void computePrefixFunction(int m);
};

#endif // KMP_H

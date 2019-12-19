#include "brute-force.h"


BruteForce::BruteForce()
{

}

BruteForce::~BruteForce()
{

}

void BruteForce::setAttr(QString p, QString t)
{
    this->p = p;
    this->t = t;
}

void BruteForce::run()
{
    int n = t.length();
    int m = p.length();
    double preTime = 0.0, matchTime = 0.0;

    emit returnPreTime(preTime);    // BF算法不需要预处理时间

    auto start = system_clock::now();
    QString result = "";            // reuslt存结果匹配的位置

    for (int i = 0; i <= n - m; i++) {
        bool flag = true;
        for (int j = 0; j < m; j++) {
            if(p[j] != t[i + j]){
                flag = false;
                break;
            }
        }

        if(flag){
            if(result != ""){
                result += ",";
            }
            result += QString::number(i);
        }
    }

    auto end = system_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    matchTime = double(duration.count()) * microseconds::period::num / microseconds::period::den;

    emit returnMatchTime(matchTime);
    emit returnTotalTime(preTime + matchTime);
    emit returnResults(result);
}





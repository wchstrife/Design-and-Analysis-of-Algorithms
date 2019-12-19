#include "kmp.h"

KMP::KMP()
{

}

KMP::~KMP()
{

}

void KMP::setAttr(QString p, QString t)
{
    this->p = "#" + p;
    this->t = "#" + t;
}

// KMP算法
void KMP::run()
{
    int n = t.length() - 1;
    int m = p.length() - 1;
    double preTime = 0.0, matchTime = 0.0;

    // 预处理-计算前缀数组时间
    auto start = system_clock::now();
    computePrefixFunction(m);
    auto end = system_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    preTime = double(duration.count()) * microseconds::period::num / microseconds::period::den;

    emit returnPreTime(preTime);

    start = system_clock::now();
    QString result = "";
    int q = 0;

    for(int i = 1; i <= n; i++){
        while(q > 0 && p[q + 1] != t[i]){
            q = pre[q];
        }
        if(p[q + 1] == t[i])
            q = q + 1;
        if(q == m){
            if (result != "")
                result += ",";
            result += QString::number(i - m);
            q = pre[q];
        }
    }

    end = system_clock::now();
    duration = duration_cast<microseconds>(end - start);
    matchTime = double(duration.count()) * microseconds::period::num / microseconds::period::den;

    emit returnMatchTime(matchTime);
    emit returnTotalTime(preTime + matchTime);
    emit returnResults(result);
}

// 计算前缀数组
void KMP::computePrefixFunction(int m)
{
    pre[1] = 0;
    int k = 0;
    for (int i = 2; i <= m; i++) {
        while(k > 0 && pre[k+1] != pre[i]){
            k = pre[k];
        }
        if(p[k + 1] == p[i]){
            k += 1;
        }

        pre[i] = k;
    }
}


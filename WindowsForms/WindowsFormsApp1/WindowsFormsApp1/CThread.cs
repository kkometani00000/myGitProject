using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CThread
    {
        public static void MainThread()
        {
            GetThread();
        }

        private static void GetThread()
        {
            Debug.WriteLine($"");
            Debug.WriteLine($"GetThread() -Start");

            // メインスレッドからアクセスできる変数を定義します。これに結果を格納します。
            string result = "";
            Thread thread = new Thread(new ThreadStart(() =>
            {
                // メインスレッドとは異なるスレットでHeavyMethodを実行して、
                // 結果(hoge)をresultに格納します。
                result = HeavyMethod1();
            }));

            // スレッドを開始します。
            thread.Start();

            // HeavyMethod2を実行します。
            HeavyMethod2();

            // Joinメソッドを使うとスレッドが終了するまで、これより先のコードに
            // 進まないようになります。
            thread.Join();

            // 結果をコンソールに表示します。
            Debug.WriteLine(result);

            Debug.WriteLine($"GetThread() -End");
        }

        private static String HeavyMethod1()
        {
            Debug.WriteLine($"すごく重い処理その1(´・ω・｀)はじまり");
            Thread.Sleep(500);
            Debug.WriteLine($"すごく重い処理その1(´・ω・｀)おわり");
            return "hoge";
        }

        private static void HeavyMethod2()
        {
            Debug.WriteLine($"すごく重い処理その2(´・ω・｀)はじまり");
            Thread.Sleep(300);
            Debug.WriteLine($"すごく重い処理その2(´・ω・｀)おわり");
        }
    }
}

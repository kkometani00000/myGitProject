using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CTack
    {
        public static void MainTask()
        {
            SetAsync();
            Debug.WriteLine("\n** Sample1 **");
            Sample1Main(10);
            Debug.WriteLine("\n\n** Sample2 **");
            Sample2Main(10);
        }

        private static async void SetAsync()
        {
            Task<int> task1 = CTack.CalculateAsync();
            Task<int> task2 = CTack.CalculateAsync();
            int[] results = await Task.WhenAll(task1, task2);
        }

        private static async Task<int> CalculateAsync()
        {
            return await Task.Run(() =>
            {
                // 計算処理
                return 42;
            });
        }

        private static void Sample1Main(int i)
        {
            // Task1
            //Action del_func_inst = Sample1hoge1("Sample1");
            Task s1t1 = new Task(() => { Sample1hoge1(i, "Sample1"); });
            s1t1.Start();

            // Task3
            Task s1t3 = new Task(() => { Sample1hoge3(i, "Sample1"); });
            s1t3.Start();

            // hoge2
            Sample1hoge2(i, "Sample1");

            s1t1.Wait();
            s1t3.Wait();

            return;
        }

        private static void Sample2Main(int i)
        {
            // Task1
            Task s2t1 = new Task(() => { Sample1hoge1(i, "Sample2"); });
            s2t1.Start();
            s2t1.Wait();

            // hoge2
            Sample1hoge2(i, "Sample2");

            return;
        }

        private static void Sample1hoge1(int e, string ss)
        {
            for (int i = 0; i < e; i++) Debug.WriteLine($"{ss}hoge1 is called. {i}");
            return;
        }

        private static void Sample1hoge2(int e, string ss)
        {
            for (int i = 0; i < e; i++) Debug.WriteLine($"\t{ss}hoge2 is called. {i}");
            return;
        }

        private static void Sample1hoge3(int e, string ss)
        {
            for (int i = 0; i < e; i++) Debug.WriteLine($"\t\t{ss}hoge3 is called. {i}");
            return;
        }
    }
}

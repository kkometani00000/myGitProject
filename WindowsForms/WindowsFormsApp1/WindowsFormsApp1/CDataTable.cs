using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;

namespace WindowsFormsApp1
{
    internal static class CDataTable
    {
        public static void MainDataTable()
        {
            List<DataRow> listDr = GetDataTable();
        }

        private static List<DataRow> GetDataTable()
        {
            DataTable table = new DataTable("Table");

            // カラム名の追加
            table.Columns.Add("教科");
            table.Columns.Add("点数", Type.GetType("System.Int32"));
            table.Columns.Add("氏名");
            table.Columns.Add("クラス名");

            // Rows.Addメソッドを使ってデータを追加
            table.Rows.Add("国語", 90, "田中　一郎", "A");
            table.Rows.Add("数学", 80, "田中　一郎", "A");
            table.Rows.Add("英語", 70, "田中　一郎", "A");
            table.Rows.Add("国語", 60, "鈴木　二郎", "A");
            table.Rows.Add("数学", 50, "鈴木　二郎", "A");
            table.Rows.Add("英語", 80, "鈴木　二郎", "A");
            table.Rows.Add("国語", 70, "佐藤　三郎", "B");
            table.Rows.Add("数学", 80, "佐藤　三郎", "B");
            table.Rows.Add("英語", 90, "佐藤　三郎", "B");

            // LINQを使ってデータを抽出
            var list = table.AsEnumerable().Where(x => x["氏名"].ToString() == "鈴木　二郎").ToList();

            return list;
        }
    }
}

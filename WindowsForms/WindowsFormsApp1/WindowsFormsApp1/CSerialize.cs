using System.Threading.Tasks;
using System.Xml;
using System.Text.Json;
using System.Text.Json.Serialization;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Linq;
using System.Diagnostics;

namespace WindowsFormsApp1
{
    internal static class CSerialize
    {
        public static void MainSerialize()
        {
            List<string> list = new List<string> { "abc", "123" };
            Dictionary<string, string> dic = list.Select((x, i) => new { data = x, no = i.ToString() }).ToDictionary(x => x.data, y => y.no);

            string json = ToSerialize(dic);
            var dic2 = ToDeserialize(json);

            Debug.WriteLine("");
            Debug.WriteLine("Serialize");
            dic2.Count(x => { Debug.WriteLine(x); return true; });
        }

        /// <summary>
        /// 入力をJSON文字列に変換します。
        /// </summary>
        /// <param name="dict">Dictionary<string, string>型の入力</param>
        /// <returns>JSON文字列</returns>
        private static string ToSerialize(Dictionary<string, string> dic)
        {
            var json = JsonSerializer.Serialize(dic);
            return json;
        }

        /// <summary>
        /// 入力をJSON文字列に変換します。
        /// </summary>
        /// <param name="dict">Dictionary<string, string>型の入力</param>
        /// <returns>JSON文字列</returns>
        private static Dictionary<string, string> ToDeserialize(string json)
        {
            var dic = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
            return dic;
        }
    }
}

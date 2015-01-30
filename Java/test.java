package test;

import java.sql.*;
// java通过jdbc连接mysql示例

public class test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 驱动程序名
        String driver = "com.mysql.jdbc.Driver";
        // URL指向要访问的数据库名scutcs
        String url = "jdbc:mysql://192.168.1.108:3306/Wuxia";
        String user = "appleface"; 
        String password = "root";
        
        try { 
        	Class.forName(driver);
        	Connection conn = DriverManager.getConnection(url, user, password);
        	if(!conn.isClosed()) {
        		System.out.println("Succeeded connecting to the Database!");
        	}
        	// statement用来执行SQL语句
        	Statement statement = conn.createStatement();
        	// 要执行的SQL语句
        	String sql = "select * from STUDENT";
        	// 结果集
        	ResultSet rs = statement.executeQuery(sql);
        	String name = null;
        	while(rs.next()) {
        		// 选择sname这列数据
        		name = rs.getString("sname");
        		// 首先使用ISO-8859-1字符集将name解码为字节序列并将结果存储新的字节数组中。
                // 然后使用GB2312字符集解码指定的字节数组
                name = new String(name.getBytes("ISO-8859-1"),"GB2312");
                System.out.println(rs.getString("sno") + "\t" + name);
        	}
        	rs.close();
        	conn.close();
        }catch(ClassNotFoundException e) {
        	System.out.println("Sorry,can`t find the Driver!"); 
        	e.printStackTrace();
        }catch(SQLException e) {
        	e.printStackTrace();
        }catch(Exception e) {
        	e.printStackTrace();
        }
	}

}











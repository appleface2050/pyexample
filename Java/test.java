package test;

import java.sql.*;
// javaͨ��jdbc����mysqlʾ��

public class test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// ����������
        String driver = "com.mysql.jdbc.Driver";
        // URLָ��Ҫ���ʵ����ݿ���scutcs
        String url = "jdbc:mysql://192.168.1.108:3306/Wuxia";
        String user = "appleface"; 
        String password = "root";
        
        try { 
        	Class.forName(driver);
        	Connection conn = DriverManager.getConnection(url, user, password);
        	if(!conn.isClosed()) {
        		System.out.println("Succeeded connecting to the Database!");
        	}
        	// statement����ִ��SQL���
        	Statement statement = conn.createStatement();
        	// Ҫִ�е�SQL���
        	String sql = "select * from STUDENT";
        	// �����
        	ResultSet rs = statement.executeQuery(sql);
        	String name = null;
        	while(rs.next()) {
        		// ѡ��sname��������
        		name = rs.getString("sname");
        		// ����ʹ��ISO-8859-1�ַ�����name����Ϊ�ֽ����в�������洢�µ��ֽ������С�
                // Ȼ��ʹ��GB2312�ַ�������ָ�����ֽ�����
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











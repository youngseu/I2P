# coding=utf-8
import MySQLdb
from I2P import config


class BaseDB:
    cursor = None
    db = None

    def __init__(self, dbname):
        self.db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=dbname)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    # 查询表中某属性所有值
    def get_attribute(self, table, attribute):
        sql = "SELECT " + attribute + " FROM " + table
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("get_attribute error")
            return True
        result = self.cursor.fetchall()
        # print(result)
        # for one in result:
        #     print(one[0])
        # 返回属性元组
        return result

    # 获得一定范围内的数据,用于info表中
    def get_data_range(self, table, start, end):
        sql = "SELECT * FROM " + table + " WHERE id>=" + str(start) + " AND id <=" + str(end)
        try:
            # excute
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("get_data_range error")
        result = self.cursor.fetchall()
        return result

    # 查找ip是否已经存在,用于info表中
    def judge_ip_exist(self, ip):
        sql = "SELECT id FROM ipAndLocation.info WHERE ip ='" + str(ip) + "'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("judge_ip_exist error")
            return True
        result = self.cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    # 包含位置信息的表info,用于info表
    def insert_ip(self, ip, lat, lng):
        id = self.get_max_id("info")
        sql = "INSERT INTO ipAndLocation.info (id, ip, lat, lng) VALUES ('%d','%s','%f','%f')" % \
              (id + 1, ip, lat, lng)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("insert_ip error")

    # 表all_info数据
    def add_data(self, table, id_hash, ip, port, isflood):
        id = self.get_max_id(table)
        if not self.judge_ip(table, ip):
            sql = "INSERT INTO " + table + " (id, hash,ip,port,isflood) VALUES ('%d','%s','%s','%d','%d')" % \
                                           (id + 1, id_hash, ip, port, isflood)
            print(sql)
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
                print("insert data error!")

    # 获得最大ID值,不是总记录数
    def get_max_id(self, table):
        sql = "SELECT max(id) FROM " + table
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("get_max_id error")
        result = self.cursor.fetchall()
        for res in result:
            if res[0] is None:
                return 0
            else:
                return res[0]

    # 查找总记录数
    def get_num(self, table):
        sql = "SELECT count(1) FROM " + table
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("get_num error")
        result = self.cursor.fetchone()
        if result is None:
            return 0
        else:
            return result

    # 查找table中hash是否存在
    def judge_hash_exist(self, table, id_hash):
        sql = "SELECT hash FROM " + table + " WHERE hash ='" + str(id_hash) + "'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("judge_ip_exist error")
            return True
        result = self.cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    # record数据的插入,用于数据中node_*和floodfill_*
    def insert_data(self, table, id_hash, ip):
        id = self.get_max_id(table)
        if not self.judge_hash_exist(table, id_hash):
            sql = "INSERT INTO " + table + " (id, hash,ip) VALUES ('%d','%s','%s')" % \
                                           (id + 1, id_hash, ip)
            print(sql)
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
                print("insert data error!")

    # 插入leasesets数据到hidenserver
    def insert_leaseset(self, table, lease):
        num = self.get_max_id(table)
        if not self.judge_leaseset(config.DB_LEASESET, lease):
            sql = "INSERT INTO " + table + " (id,leaseset) VALUES ('%d','%s')" % \
                                           (num + 1, lease)
            print sql
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
                print("insert data error!")

    def judge_leaseset(self, table, lease):
        sql = "SELECT leaseset FROM " + table + " WHERE leaseset ='" + str(lease) + "'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("judge_leaseset error")
            return True
        result = self.cursor.fetchone()
        if result is None:
            return False
        else:
            return True

    # 判断table中是否存在ip
    def judge_ip(self, table, ip):
        sql = "SELECT id FROM " + table + " WHERE ip ='" + str(ip) + "'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("judge_ip_exist error")
            return True
        result = self.cursor.fetchone()
        # print(result)
        # 存在返回true,不存在false
        if result is None:
            return False
        else:
            return True


if __name__ == '__main__':
    db = BaseDB()
    if db.judge_ip(config.DB_RESEED_FLOODFILL, "128.208.4.99"):
        print("reseed exit")
    if db.judge_ip(config.DB_LOOKUP_FLOODFILL, "128.208.4.99"):
        print("search exit")
    db = BaseDB()
    if db.judge_ip(config.DB_ALLINFO, "213.167.240.113"):
        print("reseed exit")
    print(db.get_attribute("info", "*"))

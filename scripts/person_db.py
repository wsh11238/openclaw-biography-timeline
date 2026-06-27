#!/usr/bin/env python3
"""预置人物数据库 — 知名人物预填充研究数据，减少重复网络搜索。

已入库人物（9人）：
  政治: 毛泽东、邓小平、周恩来、朱德、刘少奇
  科技: 任正非、马云
  科学: 钱学森、杨振宁
数据来源: 维基百科（中英文）、百度百科、大英百科全书
"""

PERSON_DB = {

    "毛泽东": {
    "subject": {
        "name": "毛泽东",
        "native_name": "Mao Zedong",
        "identifiers": [
            "中国",
            "政治家",
            "革命家",
            "中共中央主席"
        ],
        "fields": [
            "马克思主义",
            "无产阶级革命",
            "军事战略",
            "理论家"
        ],
        "date_range": "1893-1976",
        "birth_date": "1893-12",
        "birth_display": "1893年12月26日",
        "current_age": "享年82岁",
        "portrait_url": ""
    },
    "summary": [
        "中国共产党、中华人民共和国和中国人民解放军的主要缔造者，中国第一代最高领导人。",
        "将马克思主义中国化，创立毛泽东思想，指导中国革命从胜利走向胜利。"
    ],
    "events": [
        {
            "date": "1893-12-26",
            "title": "诞生",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1918",
            "title": "毕业于湖南第一师范学校",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1921-07",
            "title": "出席中共一大",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1927-08",
            "title": "八七会议提出「枪杆子里面出政权」",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1927-09",
            "title": "领导秋收起义，上井冈山",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1928-04",
            "title": "与朱德井冈山会师",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1935-01",
            "title": "遵义会议确立领导地位",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1934-10",
            "title": "参加长征",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1937-07",
            "title": "抗日战争全面爆发，部署敌后游击战",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1945-06",
            "title": "中共七届一中全会当选中央委员会主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1949-10-01",
            "title": "中华人民共和国成立，当选中央人民政府主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1950-10",
            "title": "决策抗美援朝",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1954-09",
            "title": "当选首任中华人民共和国主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1958",
            "title": "发动大跃进",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1966",
            "title": "发动文化大革命",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1972-02",
            "title": "会见尼克松，中美关系正常化",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1976-09-09",
            "title": "在北京逝世",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "毛泽东生平",
            "publisher": "天下韶山网",
            "url": "https://www.txssw.com/channel/29117.html",
            "tier": "encyclopedia"
        },
        {
            "id": "S2",
            "title": "毛泽东（维基百科）",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Mao_Zedong",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "毛泽东生平年表",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/毛泽东生平",
            "tier": "wikipedia"
        },
        {
            "id": "S4",
            "title": "毛泽东（百度百科）",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/毛泽东/11365",
            "tier": "baidu-baike"
        },
        {
            "id": "S5",
            "title": "中华人民共和国国史百科全书（1949-1999）",
            "publisher": "中国大百科全书出版社",
            "tier": "encyclopedia"
        },
        {
            "id": "S6",
            "title": "Mao Zedong",
            "publisher": "Britannica",
            "url": "https://www.britannica.com/biography/Mao-Zedong",
            "tier": "encyclopedia"
        },
        {
            "id": "S7",
            "title": "毛泽东原专职图书管理员谈主席晚年读书生活",
            "publisher": "天下韶山网",
            "url": "https://maozedong.com/?id=223",
            "tier": "reference"
        },
        {
            "id": "S8",
            "title": "崇高理想、光辉思想、伟大功绩",
            "publisher": "天下韶山网",
            "url": "https://maozedong.com/?id=268",
            "tier": "reference"
        }
    ],
    "life_stages": [
        {
            "period": "1893-1910",
            "age_range": "0-17岁",
            "title": "韶山少年",
            "description": "生于湖南湘潭，幼年接受传统儒家教育。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1910-1921",
            "age_range": "17-28岁",
            "title": "求学与革命启蒙",
            "description": "在湖南一师接受新式教育，参加辛亥革命，接触马克思主义。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1921-1935",
            "age_range": "28-42岁",
            "title": "建党与井冈山",
            "description": "参与建党，领导农民运动，创建第一个农村革命根据地。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1935-1949",
            "age_range": "42-56岁",
            "title": "长征与建国",
            "description": "遵义会议确立领导地位，指挥抗日战争和解放战争，建立新中国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949-1976",
            "age_range": "56-83岁",
            "title": "执政与晚年",
            "description": "领导社会主义建设，发动文化大革命，1976年逝世。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1921年",
            "title": "参与创建中国共产党",
            "choice": "出席中共一大，确立以农村为基础的革命路线。",
            "consequence": "中国革命有了坚强的领导核心，开启农村包围城市的道路。",
            "dark_side_or_failure": "建党初期力量薄弱，多次遭受镇压。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1927年",
            "title": "枪杆子里面出政权",
            "choice": "在八七会议上提出用武装革命夺取政权。",
            "consequence": "开始独立领导武装斗争，走上井冈山道路。",
            "dark_side_or_failure": "早期红军力量弱小，根据地多次失守。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1935年",
            "title": "遵义会议确立领导地位",
            "choice": "在遵义会议被增补为中央政治局常委。",
            "consequence": "结束了左倾路线统治，挽救了党、红军和中国革命。",
            "dark_side_or_failure": "此前被左倾路线排挤，第五次反围剿失败。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949年",
            "title": "中华人民共和国成立",
            "choice": "在天安门城楼宣告新中国成立。",
            "consequence": "中国人民从此站起来了，开启社会主义建设历程。",
            "dark_side_or_failure": "建国后面临经济恢复、抗美援朝等严峻考验。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1966年",
            "title": "发动文化大革命",
            "choice": "发动文革，试图防止资本主义复辟。",
            "consequence": "给党、国家和人民造成严重灾难，十年动乱。",
            "dark_side_or_failure": "被反革命集团利用，造成巨大损失。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高职务",
                "value": "中共中央委员会主席",
                "description": "1945-1976年连续执政31年",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "核心贡献",
                "value": "新中国缔造者",
                "description": "领导中国共产党建立中华人民共和国",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "理论遗产",
                "value": "毛泽东思想",
                "description": "马克思主义中国化的第一个理论成果",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "历史争议",
                "value": "文化大革命",
                "description": "1966-1976年文革造成严重损失",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "建国功勋",
                "title": "缔造中华人民共和国",
                "description": "领导中国共产党和人民军队，经过28年斗争，建立新中国，结束半殖民地半封建社会。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "type": "controversy",
                "label": "历史争议",
                "title": "文化大革命",
                "description": "1966-1976年发动文革，被林彪、江青反革命集团利用，造成十年浩劫。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "毛泽东",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "朱德",
                "type": "collaborator",
                "relation": "井冈山会师战友",
                "description": "红四军军长，与毛泽东并称朱毛，解放后任国家副主席、国防部长。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "周恩来",
                "type": "collaborator",
                "relation": "长期搭档",
                "description": "建国后长期担任国务院总理，是毛泽东最重要的政治伙伴。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "刘少奇",
                "type": "competitor",
                "relation": "政治对手",
                "description": "文革中被批斗致死，曾是毛泽东选定的接班人。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "林彪",
                "type": "competitor",
                "relation": "反革命集团",
                "description": "被确定为毛泽东的接班人，后策划政变失败出逃，机毁人亡。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1911-1949",
            "title": "新民主主义革命",
            "context": "辛亥革命后军阀割据，中华民族面临帝国主义侵略和封建压迫。",
            "breakthrough": "以农村包围城市、最后夺取城市的战略，带领中国共产党取得革命胜利。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949-1976",
            "title": "社会主义建设与探索",
            "context": "新中国成立，百废待兴，同时面临西方封锁和苏联大国主义压力。",
            "breakthrough": "领导土地改革、抗美援朝、三大改造，探索中国社会主义建设道路。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "政治",
                "title": "中国社会主义制度的奠基人",
                "description": "领导建立中国共产党领导的人民民主专政，确立社会主义基本制度。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "军事",
                "title": "人民军队的缔造者",
                "description": "提出人民战争理论，建立党指挥枪的原则，人民解放军成为国家柱石。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "思想",
                "title": "毛泽东思想",
                "description": "马克思主义中国化第一次历史性飞跃，是中国共产党长期坚持的指导思想。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "政治影响力",
            "description": "以党内地位、军队控制力和国际声望为相对指标。",
            "points": [
                {
                    "period": "1921年",
                    "label": "建党初期",
                    "value": 15
                },
                {
                    "period": "1935年",
                    "label": "遵义会议",
                    "value": 45
                },
                {
                    "period": "1945年",
                    "label": "七大确立",
                    "value": 70
                },
                {
                    "period": "1949年",
                    "label": "建国",
                    "value": 95
                },
                {
                    "period": "1966年",
                    "label": "文革顶峰",
                    "value": 100
                },
                {
                    "period": "1976年",
                    "label": "逝世",
                    "value": 80
                }
            ]
        }
    ],
    "epitaph": {
        "text": "中国共产党和中华人民共和国的主要缔造者，中国革命和社会主义建设事业的伟大领袖。",
        "source_ids": [
            "S1",
            "S2"
        ]
    },
    "uncertainty_notes": [
        "文革期间具体伤亡数字各来源差异较大，以官方口径为准。",
        "晚年健康状况细节官方未全面公开，部分时间线依据公开报道推断。"
    ],
    "source_notes": [
        "以天下韶山网（湖南省韶山管理局）和维基百科为主要来源。",
        "重大事件与官方表述保持一致，争议事件标注来源分歧。"
    ]
},

    "邓小平": {
    "subject": {
        "name": "邓小平",
        "native_name": "Deng Xiaoping",
        "identifiers": [
            "中国",
            "政治家",
            "改革开放总设计师",
            "革命家"
        ],
        "fields": [
            "政治",
            "经济改革",
            "外交",
            "理论"
        ],
        "date_range": "1904-1997",
        "birth_date": "1904-08-22",
        "birth_display": "1904年8月22日",
        "current_age": "享年93岁",
        "portrait_url": ""
    },
    "summary": [
        "中国改革开放和现代化建设的总设计师，中国特色社会主义理论的开创者。",
        "历经三落三起，1978年后成为中国共产党第二代领导核心，带领中国走向市场经济改革。"
    ],
    "events": [
        {
            "date": "1904-08-22",
            "title": "出生于四川广安",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1920-10",
            "title": "赴法国勤工俭学，在工厂做工期间接触马克思主义",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1924",
            "title": "加入中国共产主义青年团欧洲支部，后转入中国共产党",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1926",
            "title": "赴莫斯科中山大学留学",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1929-12",
            "title": "领导百色起义，创建红七军",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1933",
            "title": "因支持毛泽东路线被撤销职务，第一次被打倒",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1934-10",
            "title": "参加长征",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1935-01",
            "title": "参加遵义会议",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1938-01",
            "title": "任八路军129师政委，与刘伯承搭档开辟太行山根据地",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1948-11",
            "title": "参与指挥淮海战役，任总前委书记",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1949-10",
            "title": "参加开国大典，后任西南局第一书记",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1952",
            "title": "调任中央，任政务院副总理",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1956-09",
            "title": "中共八大当选中央委员会总书记",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1966",
            "title": "文化大革命中被作为「第二号走资派」打倒，第二次被打倒",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1973",
            "title": "恢复国务院副总理职务，复出政坛",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1976-04",
            "title": "因天安门事件第三次被打倒，撤销党内外一切职务",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1977-07",
            "title": "中共十届三中全会恢复全部职务，第三次复出",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1978-12",
            "title": "中共十一届三中全会确立改革开放路线，成为领导核心",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1979",
            "title": "提出创办经济特区，深圳、珠海、汕头、厦门获批",
            "category": "经济",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1982-09",
            "title": "中共十二大提出「建设有中国特色的社会主义」",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1984-12",
            "title": "签署中英联合声明，确定香港回归及「一国两制」方针",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1992-01",
            "title": "南巡讲话，推动深化改革，确立市场经济方向",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1997-02-19",
            "title": "在北京逝世",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "邓小平",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/邓小平",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Deng Xiaoping",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Deng_Xiaoping",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "邓小平",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/邓小平",
            "tier": "baidu-baike"
        },
        {
            "id": "S4",
            "title": "Deng Xiaoping",
            "publisher": "Britannica",
            "url": "https://www.britannica.com/biography/Deng-Xiaoping",
            "tier": "encyclopedia"
        }
    ],
    "life_stages": [
        {
            "period": "1904-1920",
            "age_range": "0-16岁",
            "title": "广安少年",
            "description": "生于四川广安，幼年接受传统教育，1919年在重庆求学，受五四运动影响。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1920-1927",
            "age_range": "16-23岁",
            "title": "留法勤工俭学与入党",
            "description": "赴法国勤工俭学，在工厂做工期间接触马克思主义，结识周恩来等人，1924年加入中共，后赴莫斯科学习。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1927-1949",
            "age_range": "23-45岁",
            "title": "革命战争岁月",
            "description": "领导百色起义，参加长征，任八路军129师政委，参与指挥淮海战役和渡江战役。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1949-1966",
            "age_range": "45-62岁",
            "title": "建国后执政",
            "description": "任西南局第一书记，后调中央任副总理、总书记，参与国家建设决策。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1966-1977",
            "age_range": "62-73岁",
            "title": "文革三落三起",
            "description": "三次被打倒、三次复出，在拖拉机厂劳动改造后重返政坛。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1978-1997",
            "age_range": "74-93岁",
            "title": "改革开放总设计师",
            "description": "确立改革开放路线，创办经济特区，提出一国两制，推动市场经济改革。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1924年",
            "title": "在法国加入中共",
            "choice": "在法国勤工俭学期间选择加入中国共产党。",
            "consequence": "走上职业革命家道路，结识周恩来等早期中共领导人。",
            "dark_side_or_failure": "放弃了正常的求学和职业道路，投身充满危险的革命事业。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1933年",
            "title": "第一次被打倒",
            "choice": "因支持毛泽东的正确路线而被「左」倾路线打击。",
            "consequence": "被撤销职务，但此后在遵义会议后恢复地位，与毛泽东的政治联盟加深。",
            "dark_side_or_failure": "妻子因政治打击而离开他，个人生活受到重创。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1978年",
            "title": "十一届三中全会确立领导核心",
            "choice": "在粉碎四人帮后通过斗争成为实际最高领导人，推动改革开放。",
            "consequence": "中国从计划经济转向社会主义市场经济，开启四十年经济高速增长。",
            "dark_side_or_failure": "改革过程中也出现了通货膨胀、腐败等问题，1989年事件成为其政治遗产的争议点。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1992年",
            "title": "南巡讲话",
            "choice": "88岁高龄南巡深圳等地，发表系列讲话推动深化改革。",
            "consequence": "打破改革停滞局面，确立社会主义市场经济方向，中国经济迎来新一轮高速增长。",
            "dark_side_or_failure": "改革加速也带来了贫富分化等社会问题。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高职务",
                "value": "中央军委主席",
                "description": "1981-1989年任中央军委主席，实际最高领导人",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "核心贡献",
                "value": "改革开放总设计师",
                "description": "带领中国从计划经济转向市场经济，实现经济腾飞",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "理论遗产",
                "value": "邓小平理论",
                "description": "中国特色社会主义理论体系的开创者",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "政治传奇",
                "value": "三落三起",
                "description": "三次被打倒、三次复出，政治生命极其坚韧",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "改革开放",
                "title": "带领中国走向市场经济",
                "description": "推动改革开放，创办经济特区，确立社会主义市场经济方向，使中国成为世界第二大经济体。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "achievement",
                "label": "一国两制",
                "title": "解决香港澳门问题",
                "description": "提出「一国两制」方针，实现香港、澳门和平回归。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "历史争议",
                "title": "八九事件",
                "description": "1989年下令对天安门广场抗议活动进行武力清场，造成人员伤亡，成为其政治遗产中最大争议。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "邓小平",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "毛泽东",
                "type": "collaborator",
                "relation": "上级与战友",
                "description": "长征时期支持毛泽东路线，建国后任总书记，文革中三起三落与毛的关系变化密切相关。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "周恩来",
                "type": "collaborator",
                "relation": "留法时期的引路人",
                "description": "1920年代在法国结识周恩来，周是其革命道路的早期引路人。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "刘伯承",
                "type": "collaborator",
                "relation": "军事搭档",
                "description": "抗战和解放战争期间长期搭档，并称「刘邓」，共同指挥129师和第二野战军。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "陈云",
                "type": "collaborator",
                "relation": "改革同僚",
                "description": "改革开放时期的重要合作者，在经济改革路线上既有合作也有分歧。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "华国锋",
                "type": "competitor",
                "relation": "权力交接对手",
                "description": "毛逝世后与华国锋竞争最高权力，最终在十一届三中全会上确立领导地位。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1920-1949",
            "title": "革命战争年代",
            "context": "中国处于内忧外患，国共两党从合作走向对抗。",
            "breakthrough": "从留法学生成长为军事将领，参与缔造新中国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949-1976",
            "title": "毛泽东时代",
            "context": "建国后社会主义建设与政治运动交替进行。",
            "breakthrough": "三落三起中积累政治经验，为日后改革做准备。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1978-1997",
            "title": "改革开放时代",
            "context": "文革结束后百废待兴，中国面临发展道路抉择。",
            "breakthrough": "推动改革开放，建立市场经济体制，中国走向繁荣。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "经济",
                "title": "改革开放总设计师",
                "description": "推动中国从计划经济转向市场经济，使数亿人脱贫，中国成为世界第二大经济体。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "政治",
                "title": "中国特色社会主义理论",
                "description": "创立邓小平理论，提出社会主义初级阶段理论和一国两制方针。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "外交",
                "title": "中美关系正常化推动者",
                "description": "推动中美建交，改善中国外部环境，为中国发展创造有利国际条件。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "政治影响力",
            "description": "以党内地位、决策权和历史影响为相对指标。",
            "points": [
                {
                    "period": "1924年",
                    "label": "加入中共",
                    "value": 15
                },
                {
                    "period": "1949年",
                    "label": "建国",
                    "value": 50
                },
                {
                    "period": "1956年",
                    "label": "八大总书记",
                    "value": 65
                },
                {
                    "period": "1966年",
                    "label": "第一次被打倒",
                    "value": 10
                },
                {
                    "period": "1973年",
                    "label": "复出",
                    "value": 45
                },
                {
                    "period": "1976年",
                    "label": "第三次被打倒",
                    "value": 5
                },
                {
                    "period": "1978年",
                    "label": "改革开放",
                    "value": 95
                },
                {
                    "period": "1992年",
                    "label": "南巡讲话",
                    "value": 100
                }
            ]
        }
    ],
    "epitaph": {
        "text": "中国改革开放和现代化建设的总设计师，中国特色社会主义理论的开创者。",
        "source_ids": [
            "S1",
            "S2",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "南巡讲话的具体日期和内容细节不同来源表述略有差异。",
        "邓小平在1989年事件中的具体决策过程官方未全面公开。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源。",
        "重大事件与官方表述基本一致，争议事件标注来源分歧。"
    ]
},

    "周恩来": {
    "subject": {
        "name": "周恩来",
        "native_name": "Zhou Enlai",
        "identifiers": [
            "中国",
            "政治家",
            "外交家",
            "国务院总理"
        ],
        "fields": [
            "政治",
            "外交",
            "军事"
        ],
        "date_range": "1898-1976",
        "birth_date": "1898-03-05",
        "birth_display": "1898年3月5日",
        "current_age": "享年78岁",
        "portrait_url": ""
    },
    "summary": [
        "中华人民共和国首任国务院总理和外交部长，中国共产党和人民军队的主要创建人之一。",
        "协助毛泽东缔造新中国，主导和平共处五项原则和中美关系破冰，被称颂为「人民的好总理」。"
    ],
    "events": [
        {
            "date": "1898-03-05",
            "title": "出生于江苏淮安",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1913-08",
            "title": "考入天津南开学校",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1917-09",
            "title": "赴日本留学，接触马克思主义",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1920-11",
            "title": "赴法国勤工俭学",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1921",
            "title": "加入巴黎共产主义小组，成为中共创建人之一",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1924-09",
            "title": "回国任黄埔军校政治部主任",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1925-08-08",
            "title": "与邓颖超在广州结婚",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1927-08-01",
            "title": "领导南昌起义，创建人民军队",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1934-10",
            "title": "参加长征",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1935-01",
            "title": "出席遵义会议，支持毛泽东确立领导地位",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1936-12",
            "title": "西安事变中作为中共代表促成和平解决",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1945-04",
            "title": "出席中共七大，当选中央政治局委员",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1949-10-01",
            "title": "任政务院总理兼外交部长",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1953-12",
            "title": "提出和平共处五项原则",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1954-04",
            "title": "率团出席日内瓦会议",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1955-04",
            "title": "出席万隆会议，提出「求同存异」方针",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1972-02-21",
            "title": "与尼克松会谈，推动中美关系正常化",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1972-09",
            "title": "与田中角荣会谈，实现中日邦交正常化",
            "category": "外交",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1975-01",
            "title": "在四届全国人大重提四个现代化目标",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1976-01-08",
            "title": "在北京逝世",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "周恩来",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/周恩来",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Zhou Enlai",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Zhou_Enlai",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "周恩来",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/周恩来",
            "tier": "baidu-baike"
        },
        {
            "id": "S4",
            "title": "Zhou Enlai",
            "publisher": "Britannica",
            "url": "https://www.britannica.com/biography/Zhou-Enlai",
            "tier": "encyclopedia"
        }
    ],
    "life_stages": [
        {
            "period": "1898-1917",
            "age_range": "0-19岁",
            "title": "淮安少年",
            "description": "生于江苏淮安，幼年丧母，由嗣母抚养，接受良好教育。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1917-1924",
            "age_range": "19-26岁",
            "title": "留法勤工俭学与建党",
            "description": "赴日、赴法留学，接触马克思主义，参与创建中共欧洲支部。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1924-1937",
            "age_range": "26-39岁",
            "title": "革命战争年代",
            "description": "任黄埔军校政治部主任，领导南昌起义，参加长征。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1937-1949",
            "age_range": "39-51岁",
            "title": "抗战与解放战争",
            "description": "在国共谈判中发挥关键作用，协助毛泽东指挥解放战争。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949-1976",
            "age_range": "51-78岁",
            "title": "总理生涯",
            "description": "任国务院总理27年，主导新中国外交，推动四个现代化。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1921年",
            "title": "加入中共",
            "choice": "在法国加入共产主义小组，成为中共创建人之一。",
            "consequence": "走上职业革命家道路，日后成为中共核心领导人。",
            "dark_side_or_failure": "放弃了正常的留学生涯，投身充满风险的革命事业。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1927年",
            "title": "领导南昌起义",
            "choice": "作为前敌委员会书记领导南昌起义。",
            "consequence": "创建人民军队，奠定周恩来在军事史上的地位。",
            "dark_side_or_failure": "起义最终失败，部队损失惨重。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1935年",
            "title": "遵义会议支持毛泽东",
            "choice": "在遵义会议上支持毛泽东的正确主张。",
            "consequence": "确立毛泽东领导地位，周恩来成为毛泽东最重要的政治伙伴。",
            "dark_side_or_failure": "此前作为最高军事领导人之一承担了反围剿失败的责任。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1972年",
            "title": "推动中美关系破冰",
            "choice": "在文革困难时期推动中美关系正常化。",
            "consequence": "改善中国外部环境，为后来的改革开放奠定外交基础。",
            "dark_side_or_failure": "文革中自身也受到冲击，不得不在政治夹缝中维持国家运转。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高职务",
                "value": "国务院总理",
                "description": "1949-1976年连任总理27年",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "核心贡献",
                "value": "新中国外交奠基人",
                "description": "提出和平共处五项原则，推动中美中日关系正常化",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "历史评价",
                "value": "人民的好总理",
                "description": "鞠躬尽瘁，死而后已，深受人民爱戴",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "外交遗产",
                "value": "求同存异",
                "description": "万隆会议提出求同存异方针，成为国际关系准则",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "外交功勋",
                "title": "新中国外交奠基人",
                "description": "提出和平共处五项原则，推动中美关系破冰，实现中日邦交正常化，为新中国打开外交局面。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "achievement",
                "label": "治国功勋",
                "title": "鞠躬尽瘁的好总理",
                "description": "任总理27年，在文革中尽力维持国家运转，保护大批干部，推动四个现代化。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "历史争议",
                "title": "文革中的角色",
                "description": "在文化大革命中周恩来被迫做了一些违心之事，但也有观点认为他在极端环境下尽力减少损失。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "周恩来",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "毛泽东",
                "type": "collaborator",
                "relation": "长期搭档",
                "description": "从遵义会议后成为毛泽东最重要的政治伙伴，长达40年的合作。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "邓颖超",
                "type": "collaborator",
                "relation": "革命伴侣",
                "description": "1925年结婚，共同走过半个世纪的革命生涯，无子女。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "邓小平",
                "type": "collaborator",
                "relation": "留法时期战友",
                "description": "1920年代在法国结识，是邓小平革命道路的早期引路人。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "朱德",
                "type": "collaborator",
                "relation": "南昌起义搭档",
                "description": "1927年共同领导南昌起义，后长期合作。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "尼克松",
                "type": "competitor",
                "relation": "外交对手转伙伴",
                "description": "1972年与尼克松会谈，推动中美关系破冰。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1898-1949",
            "title": "革命年代",
            "context": "中国处于半殖民地半封建社会，民族危亡。",
            "breakthrough": "从留学生成长为革命领袖，参与缔造新中国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1949-1976",
            "title": "建国与外交",
            "context": "新中国百废待兴，面临西方封锁和冷战格局。",
            "breakthrough": "打破外交孤立，推动中美关系正常化，为改革开放奠基。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "外交",
                "title": "和平共处五项原则",
                "description": "提出和平共处五项原则，成为国际关系基本准则，影响至今。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "政治",
                "title": "人民的好总理",
                "description": "任总理27年，鞠躬尽瘁，深受人民爱戴，成为共产党人的道德楷模。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "军事",
                "title": "人民军队创建者",
                "description": "领导南昌起义，参与创建人民军队，在军事指挥中发挥重要作用。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "政治影响力",
            "description": "以党内地位、外交成就和人民声望为相对指标。",
            "points": [
                {
                    "period": "1921年",
                    "label": "加入中共",
                    "value": 20
                },
                {
                    "period": "1927年",
                    "label": "南昌起义",
                    "value": 40
                },
                {
                    "period": "1935年",
                    "label": "遵义会议",
                    "value": 55
                },
                {
                    "period": "1949年",
                    "label": "任总理",
                    "value": 80
                },
                {
                    "period": "1955年",
                    "label": "万隆会议",
                    "value": 90
                },
                {
                    "period": "1972年",
                    "label": "中美破冰",
                    "value": 95
                },
                {
                    "period": "1976年",
                    "label": "逝世",
                    "value": 100
                }
            ]
        }
    ],
    "epitaph": {
        "text": "人民的好总理，鞠躬尽瘁，死而后已。",
        "source_ids": [
            "S1",
            "S2",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "周恩来在文革中的具体决策和行为，不同来源评价差异较大。",
        "部分外交活动的具体日期在不同来源中略有差异。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源。",
        "重大事件与官方表述保持一致，争议事件标注来源分歧。"
    ]
},

    "朱德": {
    "subject": {
        "name": "朱德",
        "native_name": "Zhu De",
        "identifiers": [
            "中国",
            "军事家",
            "革命家",
            "解放军总司令"
        ],
        "fields": [
            "军事",
            "革命",
            "政治"
        ],
        "date_range": "1886-1976",
        "birth_date": "1886-12-01",
        "birth_display": "1886年12月1日",
        "current_age": "享年90岁",
        "portrait_url": ""
    },
    "summary": [
        "中国共产党和中国人民解放军的主要缔造者之一，中华人民共和国十大元帅之首。",
        "历任红军、八路军、解放军总司令，与毛泽东并称「朱毛」，被誉为「红军之父」。"
    ],
    "events": [
        {
            "date": "1886-12-01",
            "title": "出生于四川仪陇",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1909",
            "title": "考入云南陆军讲武堂，加入同盟会",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1911-10",
            "title": "参加昆明重九起义，响应辛亥革命",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1915-12",
            "title": "参加护国战争，在棉花坡战役成名",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1917",
            "title": "任滇军旅长，参加护法战争",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1922",
            "title": "赴德国留学，经周恩来介绍加入中国共产党",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1925",
            "title": "因革命活动被德国驱逐，转赴苏联学习军事",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1927-08-01",
            "title": "参与领导南昌起义",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1928-04-28",
            "title": "井冈山会师，与毛泽东组成红四军",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1930-08",
            "title": "任红一方面军总司令、中国工农红军总司令",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1931-11",
            "title": "任中华苏维埃共和国中央革命军事委员会主席",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1934-10",
            "title": "率部开始长征",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1935-01",
            "title": "出席遵义会议，支持毛泽东",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1937-08",
            "title": "就任八路军总指挥",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1940-08",
            "title": "与彭德怀部署百团大战",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1945-04",
            "title": "中共七大作军事报告，当选中央书记处书记",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1949-10-01",
            "title": "任中国人民解放军总司令，参加开国大典",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1955-09-27",
            "title": "被授予中华人民共和国元帅军衔（排名第一）",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1959-04",
            "title": "当选全国人大常委会委员长",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1976-07-06",
            "title": "在北京逝世",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "朱德",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/朱德",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Zhu De",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Zhu_De",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "朱德",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/朱德",
            "tier": "baidu-baike"
        },
        {
            "id": "S4",
            "title": "Zhu De",
            "publisher": "Britannica",
            "url": "https://www.britannica.com/biography/Zhu-De",
            "tier": "encyclopedia"
        }
    ],
    "life_stages": [
        {
            "period": "1886-1909",
            "age_range": "0-23岁",
            "title": "贫寒求学",
            "description": "生于四川仪陇佃农家庭，幼年过继给伯父，先后就读私塾和新式学堂。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1909-1922",
            "age_range": "23-36岁",
            "title": "滇军将领",
            "description": "考入云南讲武堂，参加辛亥革命、护国战争、护法战争，官至滇军旅长。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1922-1927",
            "age_range": "36-41岁",
            "title": "转向革命",
            "description": "弃军阀生涯，赴德国加入中共，转赴苏联学习军事，1926年回国参加北伐。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1927-1937",
            "age_range": "41-51岁",
            "title": "红军总司令",
            "description": "参加南昌起义、井冈山会师，任红军总司令，指挥反围剿并参加长征。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1937-1949",
            "age_range": "51-63岁",
            "title": "抗战与解放战争统帅",
            "description": "任八路军总指挥，指挥百团大战，解放战争任解放军总司令。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1949-1976",
            "age_range": "63-90岁",
            "title": "国家领导人",
            "description": "任国家副主席、人大常委会委员长，1955年授元帅衔，文革中受冲击。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1922年",
            "title": "弃军阀投奔革命",
            "choice": "放弃高官厚禄的军阀生涯，赴德国留学并加入中共。",
            "consequence": "走上共产主义革命道路，为其后军事统帅生涯奠基。",
            "dark_side_or_failure": "入党之初遭陈独秀冷淡对待，抛下了原有社会地位。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1928年",
            "title": "井冈山会师",
            "choice": "率南昌起义余部上井冈山与毛泽东会师，组成红四军。",
            "consequence": "「朱毛」合体成为红军核心，奠定人民军队基础。",
            "dark_side_or_failure": "随后朱毛之争中毛泽东曾被免前委书记，暴露军事与政治路线分歧。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1935年",
            "title": "遵义会议支持毛泽东",
            "choice": "在遵义会议上支持毛泽东的正确主张。",
            "consequence": "确立毛泽东领导地位，扭转长征危局。",
            "dark_side_or_failure": "随后被张国焘裹挟南下，险遭不测。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1959年",
            "title": "庐山会议温和批评彭德怀",
            "choice": "在庐山会议上对彭德怀仅作温和批评而非严厉批判。",
            "consequence": "毛泽东对朱德不满，会后朱德被解除军委副主席职务。",
            "dark_side_or_failure": "未能挽救彭德怀，反使自身政治影响力下降。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高职务",
                "value": "全国人大常委会委员长",
                "description": "1959-1976年连任第二、三、四届委员长",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "军衔荣誉",
                "value": "中华人民共和国元帅",
                "description": "1955年授衔排名第一",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "历史别称",
                "value": "朱毛、红军之父",
                "description": "与毛泽东长期并称朱毛",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "最高评价",
                "value": "人民的光荣",
                "description": "1946年毛泽东题词「人民的光荣」",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "军事功勋",
                "title": "人民军队主要缔造者",
                "description": "从南昌起义到井冈山建军，始终是红军、八路军、解放军的最高军事统帅之一。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "achievement",
                "label": "军事理论",
                "title": "游击战术奠基人",
                "description": "提出「敌进我退，敌驻我扰，敌疲我打，敌退我追」十六字诀游击战术。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "历史争议",
                "title": "庐山会议与文革",
                "description": "庐山会议上未严厉批判彭德怀而被毛泽东不满；文革中受冲击被疏散至广东。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "朱德",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "毛泽东",
                "type": "collaborator",
                "relation": "革命搭档「朱毛」",
                "description": "1928年井冈山会师后并称「朱毛」，长期共同指挥红军、八路军、解放军。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "周恩来",
                "type": "collaborator",
                "relation": "入党介绍人",
                "description": "1922年在柏林介绍朱德入党，长期合作军事指挥。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "彭德怀",
                "type": "collaborator",
                "relation": "抗战战友",
                "description": "百团大战联名部署；庐山会议上朱德试图温和保护彭德怀未果。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "张国焘",
                "type": "competitor",
                "relation": "长征分裂对立者",
                "description": "长征中张国焘另立中央并裹挟朱德南下，朱德与其斗争。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "林彪",
                "type": "competitor",
                "relation": "文革中的攻击者",
                "description": "文革中林彪集团批判朱德，1969年将朱德疏散至广东。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1886-1911",
            "title": "清末求学",
            "context": "清朝内忧外患，科举将废。",
            "breakthrough": "弃科举入新式军事教育，投身反清革命。",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "period": "1911-1927",
            "title": "军阀混战",
            "context": "辛亥革命后军阀割据。",
            "breakthrough": "从滇军旅长转向马克思主义，完成由旧军人到革命者的转变。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1927-1949",
            "title": "革命战争",
            "context": "国共决裂、土地革命、抗日战争、全面内战。",
            "breakthrough": "任红军、八路军、解放军总司令，协助毛泽东赢得革命胜利。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1949-1976",
            "title": "建国时期",
            "context": "社会主义改造、大跃进、文革。",
            "breakthrough": "任国家副主席、委员长、元帅，参与国家制度建设。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "军事",
                "title": "人民军队主要缔造者",
                "description": "从南昌起义到解放战争，始终是最高军事统帅之一，奠定人民军队建军原则。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "政治",
                "title": "党和国家重要领导人",
                "description": "历任中共中央副主席、国家副主席、全国人大常委会委员长。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "革命",
                "title": "跨时代的革命典范",
                "description": "参加革命70年，跨越四个历史时期，被毛泽东誉为「人民的光荣」。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "军事影响力",
            "description": "以军事统帅地位和指挥权为相对指标。",
            "points": [
                {
                    "period": "1911年",
                    "label": "辛亥起义",
                    "value": 15
                },
                {
                    "period": "1917年",
                    "label": "滇军旅长",
                    "value": 35
                },
                {
                    "period": "1928年",
                    "label": "红四军军长",
                    "value": 60
                },
                {
                    "period": "1931年",
                    "label": "中革军委主席",
                    "value": 80
                },
                {
                    "period": "1937年",
                    "label": "八路军总指挥",
                    "value": 90
                },
                {
                    "period": "1949年",
                    "label": "解放军总司令",
                    "value": 100
                },
                {
                    "period": "1959年",
                    "label": "退出一线军职",
                    "value": 70
                },
                {
                    "period": "1976年",
                    "label": "逝世",
                    "value": 50
                }
            ]
        }
    ],
    "epitaph": {
        "text": "参加革命70年，为中国人民解放事业和社会主义建设事业建立了不朽功勋，毛泽东誉其为「人民的光荣」。",
        "source_ids": [
            "S1",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "逝世年龄存在来源差异：英文维基标注89岁（周岁），百度百科标注90岁（虚岁）。",
        "百团大战开始日期有1940年7月（部署）与8月20日（发动）两说。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源，交叉验证。",
        "重大事件与官方表述保持一致。"
    ]
},

    "刘少奇": {
    "subject": {
        "name": "刘少奇",
        "native_name": "Liu Shaoqi",
        "identifiers": [
            "中国",
            "政治家",
            "革命家",
            "理论家"
        ],
        "fields": [
            "政治",
            "工人运动",
            "党建理论"
        ],
        "date_range": "1898-1969",
        "birth_date": "1898-11-24",
        "birth_display": "1898年11月24日",
        "current_age": "享年71岁",
        "portrait_url": ""
    },
    "summary": [
        "中国共产党和中华人民共和国的主要领导人之一，曾任中华人民共和国主席和中共中央副主席。",
        "早年领导工人运动，建国后主持制定宪法，在文革中被作为「走资派」打倒，迫害致死，1980年平反。"
    ],
    "events": [
        {
            "date": "1898-11-24",
            "title": "出生于湖南宁乡",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1919",
            "title": "投身五四运动，赴北京求学",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1920-08",
            "title": "加入中国社会主义青年团",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1921-07",
            "title": "赴莫斯科东方大学留学并加入中共",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1922-09",
            "title": "领导安源路矿工人大罢工",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1925-05",
            "title": "参与五卅运动，当选全国总工会副委员长",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1927-05",
            "title": "中共五大当选中央委员",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1929",
            "title": "任中共满洲省委书记，被捕后获释",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1932",
            "title": "进入中央苏区，任中共福建省委书记",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1934-10",
            "title": "参加长征",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1935-01",
            "title": "出席遵义会议，支持毛泽东",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1936",
            "title": "任中共中央北方局书记",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1939-07",
            "title": "发表《论共产党员的修养》",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1941",
            "title": "皖南事变后任新四军政委",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1943-03",
            "title": "任中央书记处书记、军委副主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1945",
            "title": "中共七大首次系统论述毛泽东思想",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1949-10-01",
            "title": "任中央人民政府副主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1954-09",
            "title": "当选首任全国人大常委会委员长",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1956-09",
            "title": "中共八大当选中央副主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1959-04-27",
            "title": "当选中华人民共和国主席",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1962",
            "title": "七千人大会推动经济调整，与毛泽东产生分歧",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1966-08",
            "title": "文化大革命中被作为「走资派」打倒",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1968-10",
            "title": "被开除党籍，撤销一切职务",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1969-11-12",
            "title": "在开封被迫害致死",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1980-02",
            "title": "中共十一届五中全会平反",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "刘少奇",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/刘少奇",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Liu Shaoqi",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Liu_Shaoqi",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "刘少奇",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/刘少奇",
            "tier": "baidu-baike"
        },
        {
            "id": "S4",
            "title": "Liu Shaoqi",
            "publisher": "Britannica",
            "url": "https://www.britannica.com/biography/Liu-Shaoqi",
            "tier": "encyclopedia"
        }
    ],
    "life_stages": [
        {
            "period": "1898-1920",
            "age_range": "0-22岁",
            "title": "求学与启蒙",
            "description": "生于湖南宁乡，受五四运动洗礼，接触马克思主义。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1921-1927",
            "age_range": "23-29岁",
            "title": "留苏入党与工人运动",
            "description": "赴莫斯科留学并加入中共，回国后领导安源罢工、五卅运动，成为工人运动领袖。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1927-1936",
            "age_range": "29-38岁",
            "title": "白区工作与长征",
            "description": "在白区从事秘密工作，参加长征，出席遵义会议支持毛泽东。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1936-1949",
            "age_range": "38-51岁",
            "title": "抗战与解放战争",
            "description": "任北方局书记、新四军政委，1943年进入中央核心层，七大论述毛泽东思想。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1949-1966",
            "age_range": "51-68岁",
            "title": "国家领导人",
            "description": "任国家副主席、人大常委会委员长、国家主席，主持制定宪法。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1966-1969",
            "age_range": "68-71岁",
            "title": "文革受难",
            "description": "被打倒、开除党籍，在开封被迫害致死。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1921年",
            "title": "赴苏留学与加入中共",
            "choice": "选择赴莫斯科学习马克思主义并加入中共。",
            "consequence": "成为中共最早党员之一，开启职业革命家生涯。",
            "dark_side_or_failure": "放弃了世俗前程，投身地下革命。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1935年",
            "title": "遵义会议支持毛泽东",
            "choice": "在遵义会议上支持毛泽东。",
            "consequence": "确立与毛泽东的政治联盟，此后进入中共核心层。",
            "dark_side_or_failure": "这一联盟31年后因文革彻底破裂。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1962年",
            "title": "七千人大会政策分歧",
            "choice": "对大跃进困难作出清醒估计，支持经济调整方针。",
            "consequence": "推动国民经济恢复，但与毛泽东裂痕加深。",
            "dark_side_or_failure": "政策分歧最终演变为政治清算，成为文革中被打倒的深层原因。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1966年",
            "title": "文革中被彻底打倒",
            "choice": "面对文革风暴未能有效自保。",
            "consequence": "被定为「走资派」，开除党籍，最终被迫害致死。",
            "dark_side_or_failure": "作为国家主席却在政治斗争中毫无还手之力，凸显制度缺陷。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高职务",
                "value": "中华人民共和国主席",
                "description": "1959-1968年任国家主席",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "理论贡献",
                "value": "《论共产党员的修养》",
                "description": "系统阐述党员党性修养理论，成为党建经典",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "历史悲剧",
                "value": "文革中被迫害致死",
                "description": "1969年在开封逝世，以假名秘密火化",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "身后平反",
                "value": "1980年恢复名誉",
                "description": "中共十一届五中全会平反昭雪",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "工人运动",
                "title": "中共工人运动领袖",
                "description": "领导安源路矿大罢工、五卅运动，成为中共工人运动主要领导人。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "achievement",
                "label": "理论建设",
                "title": "党建理论奠基人",
                "description": "发表《论共产党员的修养》，系统论述毛泽东思想，对党建理论贡献重大。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "历史悲剧",
                "title": "文革受难",
                "description": "作为国家主席在文革中被非法打倒、迫害致死，成为中国法治建设的深刻教训。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "刘少奇",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "毛泽东",
                "type": "collaborator",
                "relation": "政治盟友转对手",
                "description": "遵义会议后结成联盟，毛视刘为接班人；大跃进后分歧加深，文革中毛主导将刘打倒。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "周恩来",
                "type": "collaborator",
                "relation": "同僚",
                "description": "同为中共核心领导人，长期共事，周主持外交行政，刘主持党务经济。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "邓小平",
                "type": "collaborator",
                "relation": "政治继承者",
                "description": "刘的经济调整路线被邓继承，文革后邓小平主导为刘平反。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "王光美",
                "type": "collaborator",
                "relation": "妻子",
                "description": "1948年结婚，文革中与刘一同遭受迫害。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "陈毅",
                "type": "collaborator",
                "relation": "新四军搭档",
                "description": "皖南事变后刘任新四军政委，与陈毅军长搭档重建新四军。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1898-1949",
            "title": "革命年代",
            "description": "从农家子弟到中共核心领导人，经历辛亥革命、五四运动、国共内战、抗日战争。",
            "breakthrough": "领导工人运动，参与缔造新中国。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1949-1966",
            "title": "建国时期",
            "description": "任国家主席，参与社会主义建设和经济调整。",
            "breakthrough": "主持制定宪法，推动经济恢复。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1966-1980",
            "title": "文革与平反",
            "description": "文革中被彻底打倒迫害致死，1980年获平反。",
            "breakthrough": "其悲剧命运推动中国法治反思。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "理论",
                "title": "党建理论经典",
                "description": "《论共产党员的修养》影响了几代党员干部教育，是党建理论的重要贡献。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "政治",
                "title": "毛泽东思想的系统论述者",
                "description": "在中共七大首次系统论述毛泽东思想，将其确立为党的指导思想。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "dimension": "法治",
                "title": "法治建设的深刻教训",
                "description": "其悲剧命运——国家主席被非法打倒迫害致死——成为中国法治建设的重要历史教训。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "政治影响力",
            "description": "从青年革命者到国家主席再到被打倒的政治轨迹。",
            "points": [
                {
                    "period": "1921年",
                    "label": "加入中共",
                    "value": 15
                },
                {
                    "period": "1922年",
                    "label": "安源罢工",
                    "value": 25
                },
                {
                    "period": "1935年",
                    "label": "遵义会议",
                    "value": 45
                },
                {
                    "period": "1943年",
                    "label": "进入核心层",
                    "value": 70
                },
                {
                    "period": "1945年",
                    "label": "七大报告",
                    "value": 80
                },
                {
                    "period": "1959年",
                    "label": "国家主席",
                    "value": 95
                },
                {
                    "period": "1966年",
                    "label": "被打倒",
                    "value": 10
                },
                {
                    "period": "1980年",
                    "label": "平反",
                    "value": 60
                }
            ]
        }
    ],
    "epitaph": {
        "text": "好在历史是人民写的。",
        "source_ids": [
            "S1",
            "S2",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "刘少奇1929年在奉天被捕是否构成「叛变」，文革中作为主要罪证，1980年平反时已被否定。",
        "逝世确切死因（肺炎/糖尿病并发症）不同来源表述略有差异。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源，三源交叉验证。",
        "关键事实在三个来源间高度一致，数据可信度高。"
    ]
},

    "任正非": {
    "subject": {
        "name": "任正非",
        "native_name": "Ren Zhengfei",
        "identifiers": [
            "华为创始人",
            "华为CEO",
            "中国企业家"
        ],
        "fields": [
            "企业管理",
            "通信技术",
            "空气动力学"
        ],
        "date_range": "1944-",
        "birth_date": "1944-10-25",
        "birth_display": "1944年10月25日",
        "current_age": "81岁",
        "portrait_url": ""
    },
    "summary": [
        "中国企业家、工程师，华为技术有限公司创始人兼首席执行官。",
        "1987年以2.1万元创立华为，将其发展为全球最大电信设备制造商，以忧患意识和灰度管理哲学著称。"
    ],
    "events": [
        {
            "date": "1944-10-25",
            "title": "出生于贵州镇宁",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1963",
            "title": "考入重庆建筑工程学院暖通专业",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1970",
            "title": "入伍基建工程兵，参与011基地飞机工厂建设",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1977",
            "title": "研制成功空气压力天平，获全军技术成果一等奖",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1978-03",
            "title": "出席全国科学大会，同年加入中国共产党",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1982",
            "title": "百万大裁军转业至深圳，当选中共十二大代表",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1983",
            "title": "任南油集团下属电子公司副总经理，被骗200万元后辞职离婚",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1987",
            "title": "43岁以2.1万元创立深圳华为技术有限公司",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1991",
            "title": "率50余名员工研发程控交换机，借高利贷维持运转",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1993",
            "title": "决定研发C&C08数字程控交换机，进军公用电信领域",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "1996",
            "title": "开拓国际市场，与李嘉诚和记电讯合作",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1998",
            "title": "完成《华为基本法》，引入IBM的IPD流程",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "2003-01",
            "title": "思科起诉华为侵权，最终达成和解",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2005",
            "title": "入选《时代》周刊世界最具影响力100人",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2011-12",
            "title": "发表《一江春水向东流》，宣布实行轮值CEO制度",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "2018-10",
            "title": "获评改革开放40年百名杰出民营企业家",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2019-05-16",
            "title": "华为被列入美国实体清单，宣布进入战时状态",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S3"
            ]
        },
        {
            "date": "2019-08",
            "title": "华为发布自有操作系统鸿蒙",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S3"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "任正非",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/任正非",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Ren Zhengfei",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Ren_Zhengfei",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "任正非",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/任正非",
            "tier": "baidu-baike"
        }
    ],
    "life_stages": [
        {
            "period": "1944-1963",
            "age_range": "0-19岁",
            "title": "贵州贫寒求学",
            "description": "出生于贵州镇宁山区，经历大跃进饥荒，高中三年未穿过衬衫，靠母亲每天一个玉米饼坚持高考。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1963-1982",
            "age_range": "19-38岁",
            "title": "军旅工程生涯",
            "description": "就读重庆建筑工程学院，入伍基建工程兵，参与辽阳石化建设，因发明空气压力天平立功。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1982-1987",
            "age_range": "38-43岁",
            "title": "深圳转业低谷",
            "description": "裁军转业至深圳南油集团，被骗200万元，辞职离婚，陷入中年危机。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1987-2000",
            "age_range": "43-56岁",
            "title": "创立华为与国内崛起",
            "description": "以2.1万元创立华为，从代销交换机起步，自主研发C&C08交换机，制定《华为基本法》。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2000-2019",
            "age_range": "56-75岁",
            "title": "全球化与抗美围剿",
            "description": "华为开拓国际市场，应对思科诉讼，推行轮值CEO制度，2019年遭美国列入实体清单。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1982年",
            "title": "放弃科研基地选择转业",
            "choice": "面对百万大裁军，选择转业南下深圳。",
            "consequence": "结束11年军旅生涯，进入商业环境，为日后创业埋下伏笔。",
            "dark_side_or_failure": "转业后被骗200万元，辞职离婚，跌入人生谷底。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1987年",
            "title": "43岁被迫创业",
            "choice": "在中年危机后集资2.1万元创立华为。",
            "consequence": "从代销交换机起步，逐步打造出全球电信巨头。",
            "dark_side_or_failure": "创业初期借高利贷发工资，员工数月未领薪。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1993年",
            "title": "豪赌C&C08数字交换机",
            "choice": "决定投入全部资金研发大型局用数字交换机。",
            "consequence": "C&C08成为华为崛起的标志性产品。",
            "dark_side_or_failure": "曾说我只有从楼上跳下去。",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "period": "2019年",
            "title": "应对美国全面封锁",
            "choice": "宣布华为进入战时状态，全面投入主航道研发。",
            "consequence": "发布鸿蒙系统、海思芯片转正。",
            "dark_side_or_failure": "海外手机业务大幅受挫。",
            "source_ids": [
                "S3"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "创业资本",
                "value": "2.1万元",
                "description": "1987年与合伙人集资创立华为",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "label": "持股比例",
                "value": "约1.42%",
                "description": "任正非仅持华为不到1.5%股份，其余由员工持股会持有",
                "source_ids": [
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "管理哲学",
                "value": "灰度理论",
                "description": "提出灰度管理哲学、狼性文化与床垫文化",
                "source_ids": [
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "成就",
                "title": "打造全球最大电信设备企业",
                "description": "将华为从2.1万元起步发展为全球最大电信设备制造商，2019年营收8588亿元。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "争议",
                "title": "与解放军关系及国家安全疑虑",
                "description": "因任正非曾服役解放军，多国将华为视为安全威胁，美国将其列入实体清单。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "任正非",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "孟晚舟",
                "type": "collaborator",
                "relation": "长女",
                "description": "华为副董事长、CFO，2018年在加拿大被逮捕。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "孙亚芳",
                "type": "collaborator",
                "relation": "前董事长",
                "description": "1993年加盟华为，曾任华为董事长。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "李一男",
                "type": "competitor",
                "relation": "前副总裁",
                "description": "华为天才工程师，出走创立港湾网络与华为竞争。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "任摩逊",
                "type": "collaborator",
                "relation": "父亲",
                "description": "曾任都匀一中校长，文革中遭批斗。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1970-1980",
            "title": "改革开放与市场化转型",
            "context": "百万大裁军释放大量技术人才进入市场。",
            "breakthrough": "任正非从军人转型为企业家。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1990-2000",
            "title": "通信产业国产化浪潮",
            "context": "中国市场被外国设备垄断。",
            "breakthrough": "华为自主研发C&C08交换机，打破外资垄断。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2018-2019",
            "title": "中美科技博弈",
            "context": "中美贸易战升级，美国围剿华为。",
            "breakthrough": "发布鸿蒙系统与海思芯片备胎转正。",
            "source_ids": [
                "S3"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "产业",
                "title": "重塑全球通信产业格局",
                "description": "华为成为全球最大电信设备商，5G技术领先全球。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "管理",
                "title": "独创中国式企业管理范式",
                "description": "灰度管理哲学、轮值CEO制度、人人股份制。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "dimension": "精神",
                "title": "忧患意识与长期主义",
                "description": "坚持每年营收10%以上投入研发，成为中国企业界奋斗标杆。",
                "source_ids": [
                    "S3"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "商业影响力",
            "description": "华为营收与全球影响力随时间增长曲线。",
            "points": [
                {
                    "period": "1987",
                    "label": "创立",
                    "value": 1
                },
                {
                    "period": "1993",
                    "label": "C&C08",
                    "value": 15
                },
                {
                    "period": "2000",
                    "label": "国际市场",
                    "value": 30
                },
                {
                    "period": "2005",
                    "label": "时代百人",
                    "value": 50
                },
                {
                    "period": "2012",
                    "label": "营收154亿",
                    "value": 70
                },
                {
                    "period": "2018",
                    "label": "营收7212亿",
                    "value": 95
                },
                {
                    "period": "2019",
                    "label": "遭美制裁",
                    "value": 80
                },
                {
                    "period": "2022",
                    "label": "营收6423亿",
                    "value": 85
                }
            ]
        }
    ],
    "epitaph": {
        "text": "以华为为载体，在全球通信技术竞争中代表中国企业从追赶到引领的历史缩影，在极限施压下展现了技术自立与战略定力的中国样本。",
        "source_ids": [
            "S1",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "任正非现任妻子身份存在不同报道。",
        "维基百科中文条目中立性存疑。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源。",
        "重大事件与公开报道一致。"
    ]
},

    "钱学森": {
    "subject": {
        "name": "钱学森",
        "native_name": "Qian Xuesen",
        "identifiers": [
            "中国航天之父",
            "中国导弹之父",
            "两弹一星元勋"
        ],
        "fields": [
            "空气动力学",
            "工程控制论",
            "火箭与航天",
            "系统科学"
        ],
        "date_range": "1911-2009",
        "birth_date": "1911-12-11",
        "birth_display": "1911年12月11日",
        "current_age": "享年97岁",
        "portrait_url": ""
    },
    "summary": [
        "中国空气动力学家与系统科学家，工程控制论创始人之一，被誉为中国航天之父与中国导弹之父。",
        "早年赴美师从冯·卡门，参与创建JPL；1955年冲破美国五年软禁回到中国，主导创建国防部第五研究院，领导中国导弹与航天工程。"
    ],
    "events": [
        {
            "date": "1911-12-11",
            "title": "出生于上海",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1929",
            "title": "考入国立交通大学机械工程系",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1934",
            "title": "毕业于交通大学，考取清华庚款留美公费生",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1935-09",
            "title": "赴美入MIT深造",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1936",
            "title": "获MIT硕士，转入加州理工师从冯·卡门",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1939",
            "title": "获加州理工博士，提出钱-卡门公式",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1943",
            "title": "参与创建加州理工喷气推进实验室（JPL）",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1945",
            "title": "以美军上校身份赴德调查纳粹火箭科技",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1947",
            "title": "与蒋英结婚，任MIT正教授",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1949",
            "title": "任加州理工学院正教授兼古根海姆中心主任",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1950",
            "title": "麦卡锡主义下被取消机密资格，遭拘禁15天",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1951-04",
            "title": "被禁止离开洛杉矶县，开始五年软禁",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1954",
            "title": "完成《工程控制论》并出版",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1955-09-17",
            "title": "登上克利夫兰总统号轮船离开美国回国",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1956",
            "title": "创建中科院力学研究所和国防部第五研究院",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1960",
            "title": "东风-1短程弹道导弹发射成功",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1970-04-24",
            "title": "中国第一颗人造卫星东方红一号发射成功",
            "category": "军事",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1991",
            "title": "获授国家杰出贡献科学家称号",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1999",
            "title": "获两弹一星功勋奖章",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2009-10-31",
            "title": "在北京逝世，享年97岁",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "钱学森",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/钱学森",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Qian Xuesen",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Qian_Xuesen",
            "tier": "wikipedia"
        }
    ],
    "life_stages": [
        {
            "period": "1911-1934",
            "age_range": "0-23岁",
            "title": "求学上海与北京",
            "description": "生于上海，就读北师大附中，考入交通大学机械工程系。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1935-1955",
            "age_range": "24-44岁",
            "title": "留美二十年",
            "description": "赴美留学，师从冯·卡门，参与创建JPL，遭麦卡锡主义迫害被软禁五年。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1955-1966",
            "age_range": "44-55岁",
            "title": "回国奠基航天",
            "description": "创建力学研究所和国防部第五研究院，领导东风导弹研制。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1966-2009",
            "age_range": "55-97岁",
            "title": "晚年荣誉",
            "description": "东方红一号发射成功，获两弹一星功勋奖章，2009年逝世。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1936年",
            "title": "转赴加州理工拜师冯·卡门",
            "choice": "取得MIT硕士后选择赴加州理工深造。",
            "consequence": "师从空气动力学权威，开启火箭研究之路。",
            "dark_side_or_failure": "在MIT期间不适应重视实验的教育方式。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1950年",
            "title": "遭麦卡锡主义迫害",
            "choice": "面对FBI调查选择不放弃回国意愿。",
            "consequence": "被软禁五年，转向工程控制论研究。",
            "dark_side_or_failure": "被拘押于特米诺岛监狱15天。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1955年",
            "title": "冲破封锁回国",
            "choice": "在艾森豪威尔批准下携家登船回国。",
            "consequence": "主导创建中国导弹与航天科研体系。",
            "dark_side_or_failure": "离美时发誓不再来美国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1956年",
            "title": "起草导弹研制方案",
            "choice": "受周恩来委托起草《建立我国国防航空工业意见书》。",
            "consequence": "促成国防部第五研究院成立。",
            "dark_side_or_failure": "初期面临人才匮乏、技术空白。",
            "source_ids": [
                "S1"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "留美时长",
                "value": "20年",
                "description": "从庚款留学生到被软禁五年",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "学术贡献",
                "value": "钱-卡门公式",
                "description": "与冯·卡门共同提出亚音速流压力修正公式",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "最高荣誉",
                "value": "两弹一星功勋奖章",
                "description": "1999年获两弹一星功勋奖章",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "成就",
                "title": "中国航天与导弹事业奠基人",
                "description": "创建国防部第五研究院，领导东风导弹和东方红卫星工程。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "type": "controversy",
                "label": "争议",
                "title": "晚年特异功能主张",
                "description": "晚年倡导研究人体特异功能、气功等，引发争议。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "钱学森",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "冯·卡门",
                "type": "collaborator",
                "relation": "博士导师",
                "description": "空气动力学权威，称钱学森为美国火箭领域最伟大的天才之一。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "蒋英",
                "type": "collaborator",
                "relation": "妻子",
                "description": "声乐家、歌唱家，1947年结婚。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "周恩来",
                "type": "collaborator",
                "relation": "政治委托人",
                "description": "委托钱学森起草导弹研制方案，文革中将其列入保护名单。",
                "source_ids": [
                    "S1"
                ]
            },
            {
                "name": "聂荣臻",
                "type": "collaborator",
                "relation": "协作元帅",
                "description": "1957年率团访苏谈判国防新技术援助。",
                "source_ids": [
                    "S1"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1930-1940",
            "title": "二战与火箭技术崛起",
            "context": "二战推动美国火箭研究。",
            "breakthrough": "钱学森参与创建JPL，赴德审讯冯·布劳恩。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1950-1955",
            "title": "冷战与麦卡锡主义",
            "context": "美国麦卡锡主义盛行。",
            "breakthrough": "钱学森被迫害软禁五年后获释回国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1956-1970",
            "title": "中国两弹一星工程",
            "context": "新中国面临核威胁。",
            "breakthrough": "钱学森创建第五研究院，领导东风导弹和东方红卫星研制成功。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "国防",
                "title": "奠定中国导弹与航天体系",
                "description": "创建国防部第五研究院，领导东风导弹和长征火箭研制。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "学科",
                "title": "创立工程控制论",
                "description": "开创工程控制论学科，推动系统工程方法在中国推广。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "人才",
                "title": "培育航天科技人才",
                "description": "参与创建中国科学技术大学，培养大批航天人才。",
                "source_ids": [
                    "S1"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "学术与国防影响力",
            "description": "从留美学者到中国航天之父的影响力演变。",
            "points": [
                {
                    "period": "1935",
                    "label": "赴美",
                    "value": 10
                },
                {
                    "period": "1939",
                    "label": "博士",
                    "value": 30
                },
                {
                    "period": "1943",
                    "label": "创建JPL",
                    "value": 50
                },
                {
                    "period": "1950",
                    "label": "遭软禁",
                    "value": 40
                },
                {
                    "period": "1955",
                    "label": "回国",
                    "value": 55
                },
                {
                    "period": "1960",
                    "label": "东风-1",
                    "value": 80
                },
                {
                    "period": "1970",
                    "label": "东方红一号",
                    "value": 90
                },
                {
                    "period": "1999",
                    "label": "两弹一星奖章",
                    "value": 100
                }
            ]
        }
    ],
    "epitaph": {
        "text": "美国火箭领域中最伟大的天才之一。——冯·卡门",
        "source_ids": [
            "S1",
            "S2"
        ]
    },
    "uncertainty_notes": [
        "出生日期存在争议：中国政府资料记为1911年12月11日。",
        "回国是否为交换朝鲜战争美军飞行员存在不同说法。"
    ],
    "source_notes": [
        "以维基百科（中英文）为主要来源。",
        "重大事件与官方表述一致。"
    ]
},

    "马云": {
    "subject": {
        "name": "马云",
        "native_name": "Jack Ma",
        "identifiers": [
            "阿里巴巴创始人",
            "风清扬",
            "马老师"
        ],
        "fields": [
            "电子商务",
            "互联网",
            "企业家",
            "公益"
        ],
        "date_range": "1964-",
        "birth_date": "1964-09-10",
        "birth_display": "1964年9月10日",
        "current_age": "61岁",
        "portrait_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/20th_Anniversary_Schwab_Foundation_Gala_Dinner_%2844887783681%29_%28cropped%29.jpg"
    },
    "summary": [
        "阿里巴巴集团、淘宝网、支付宝主要创始人，曾任阿里巴巴集团董事局主席。",
        "三次高考后毕业于杭州师范学院，缔造了中国最大的电子商务与移动支付生态体系，2014年以创纪录IPO登陆纽交所。"
    ],
    "events": [
        {
            "date": "1964-09-10",
            "title": "出生于杭州",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1982",
            "title": "首次高考落榜",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1984",
            "title": "第三次高考考入杭州师范学院",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1988",
            "title": "毕业任杭州电子工业学院英语教师",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1995",
            "title": "创办中国黄页",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1999-03",
            "title": "联合18人创办阿里巴巴",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "1999-10",
            "title": "获高盛与软银投资",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S2",
                "S3"
            ]
        },
        {
            "date": "2003-05",
            "title": "创办淘宝网，推出3年免费战略对抗eBay",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2004-12",
            "title": "创立支付宝",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2007-11",
            "title": "阿里巴巴香港上市",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "2009-09",
            "title": "创立阿里云",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S3"
            ]
        },
        {
            "date": "2009-11",
            "title": "首届双11购物节",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S3"
            ]
        },
        {
            "date": "2013-05",
            "title": "卸任阿里巴巴CEO",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2014-09-19",
            "title": "阿里巴巴纽约上市，创全球最大IPO纪录",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2018-12",
            "title": "获改革先锋称号",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S3"
            ]
        },
        {
            "date": "2019-09-10",
            "title": "卸任阿里巴巴董事局主席",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "date": "2020-10-24",
            "title": "外滩金融峰会演讲批评监管体系",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2020-11-03",
            "title": "蚂蚁集团IPO被暂缓",
            "category": "商业",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "马云",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/马云",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Jack Ma",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Jack_Ma",
            "tier": "wikipedia"
        },
        {
            "id": "S3",
            "title": "马云",
            "publisher": "百度百科",
            "url": "https://baike.baidu.com/item/马云",
            "tier": "baidu-baike"
        }
    ],
    "life_stages": [
        {
            "period": "1964-1988",
            "age_range": "0-24岁",
            "title": "杭州少年与三次高考",
            "description": "生于杭州，三次高考后考入杭州师范学院外语系。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1988-1999",
            "age_range": "24-35岁",
            "title": "英语教师到互联网创业者",
            "description": "任英语教师，创办海博翻译社和中国黄页，接触互联网。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1999-2013",
            "age_range": "35-49岁",
            "title": "阿里巴巴崛起",
            "description": "创办阿里巴巴、淘宝、支付宝，打造电商帝国。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2013-",
            "age_range": "49岁-",
            "title": "交接班与转型",
            "description": "卸任CEO和董事局主席，2020年蚂蚁IPO被叫停后转趋低调。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1995年",
            "title": "创办中国黄页",
            "choice": "赴美接触互联网后决定回国创业。",
            "consequence": "开启互联网创业之路。",
            "dark_side_or_failure": "中国黄页后被杭州电信收编。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "1999年",
            "title": "创办阿里巴巴",
            "choice": "辞去公职联合18人在杭州创办阿里巴巴。",
            "consequence": "缔造了中国最大的电子商务生态体系。",
            "dark_side_or_failure": "创业初期无人看好，曾被称为骗子。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2003年",
            "title": "秘密创办淘宝对抗eBay",
            "choice": "推出3年免费战略进入C2C市场。",
            "consequence": "两年后占据中国C2C市场70%份额。",
            "dark_side_or_failure": "免费模式意味着长期烧钱。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2020年",
            "title": "外滩演讲与蚂蚁IPO叫停",
            "choice": "公开批评金融监管体系。",
            "consequence": "蚂蚁集团IPO被暂缓，马云转趋低调。",
            "dark_side_or_failure": "从高调企业家变为低调旁观者。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "创业起点",
                "value": "1999年阿里巴巴",
                "description": "18人在杭州湖畔花园公寓创办",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "label": "最大IPO",
                "value": "250亿美元",
                "description": "2014年纽约上市创全球最大IPO纪录",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "label": "花名",
                "value": "风清扬",
                "description": "阿里花名风清扬，出自金庸小说",
                "source_ids": [
                    "S3"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "成就",
                "title": "中国电商生态缔造者",
                "description": "创办阿里巴巴、淘宝、支付宝，缔造中国最大电商与移动支付生态。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "type": "controversy",
                "label": "争议",
                "title": "蚂蚁IPO叫停与监管冲突",
                "description": "2020年外滩演讲后蚂蚁IPO被叫停，马云从高调转为低调。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "马云",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "蔡崇信",
                "type": "collaborator",
                "relation": "联合创始人",
                "description": "1999年放弃70万美元年薪加入阿里巴巴，任CFO。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "孙正义",
                "type": "collaborator",
                "relation": "投资人",
                "description": "软银创始人，2000年投资阿里巴巴2000万美元。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "name": "张勇",
                "type": "collaborator",
                "relation": "继任者",
                "description": "接替马云任阿里巴巴CEO和董事局主席。",
                "source_ids": [
                    "S1",
                    "S3"
                ]
            },
            {
                "name": "陆兆禧",
                "type": "collaborator",
                "relation": "前CEO",
                "description": "2013年接任阿里巴巴CEO，后被张勇替换。",
                "source_ids": [
                    "S1"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1995-2003",
            "title": "中国互联网起步",
            "context": "中国互联网从无到有。",
            "breakthrough": "马云创办中国黄页和阿里巴巴。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2003-2014",
            "title": "电商黄金时代",
            "context": "中国电商市场爆发式增长。",
            "breakthrough": "淘宝、支付宝、阿里云相继诞生。",
            "source_ids": [
                "S1",
                "S2",
                "S3"
            ]
        },
        {
            "period": "2014-",
            "title": "监管与转型",
            "context": "互联网监管趋严。",
            "breakthrough": "蚂蚁IPO叫停，马云转型公益。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "商业",
                "title": "中国电商生态缔造者",
                "description": "创办阿里巴巴、淘宝、支付宝，改变中国人的购物和支付方式。",
                "source_ids": [
                    "S1",
                    "S2",
                    "S3"
                ]
            },
            {
                "dimension": "技术",
                "title": "阿里云开创者",
                "description": "创立阿里云，推动中国云计算产业发展。",
                "source_ids": [
                    "S3"
                ]
            },
            {
                "dimension": "公益",
                "title": "教育与公益",
                "description": "卸任后投身教育公益，创立马云公益基金会。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "商业影响力",
            "description": "从英语教师到亚洲首富再到低调退场。",
            "points": [
                {
                    "period": "1988",
                    "label": "英语教师",
                    "value": 5
                },
                {
                    "period": "1999",
                    "label": "创办阿里",
                    "value": 15
                },
                {
                    "period": "2003",
                    "label": "淘宝",
                    "value": 35
                },
                {
                    "period": "2007",
                    "label": "香港上市",
                    "value": 55
                },
                {
                    "period": "2014",
                    "label": "纽约上市",
                    "value": 95
                },
                {
                    "period": "2019",
                    "label": "卸任",
                    "value": 80
                },
                {
                    "period": "2020",
                    "label": "蚂蚁叫停",
                    "value": 50
                }
            ]
        }
    ],
    "epitaph": {
        "text": "中国电子商务时代的开创者，以阿里巴巴和淘宝重塑了十亿人的消费方式与商业生态，将互联网从精英工具变为全民基础设施，深刻改变了中国零售业与移动支付格局。",
        "source_ids": [
            "S1",
            "S3"
        ]
    },
    "uncertainty_notes": [
        "首次高考数学分数不同来源有9分和1分两种说法。"
    ],
    "source_notes": [
        "以维基百科（中英文）和百度百科为主要来源。",
        "重大事件与公开报道一致。"
    ]
},

    "杨振宁": {
    "subject": {
        "name": "杨振宁",
        "native_name": "Yang Chen-Ning",
        "identifiers": [
            "诺贝尔物理学奖",
            "理论物理学家",
            "杨-米尔斯理论"
        ],
        "fields": [
            "理论物理",
            "粒子物理",
            "统计力学"
        ],
        "date_range": "1922-2025",
        "birth_date": "1922-10-01",
        "birth_display": "1922年10月1日",
        "current_age": "享年103岁",
        "portrait_url": ""
    },
    "summary": [
        "华裔理论物理学家，诺贝尔物理学奖获得者，杨-米尔斯理论创立者。",
        "与李政道共同提出宇称不守恒定律，1957年获诺贝尔物理学奖，是首位获此殊荣的华人科学家。"
    ],
    "events": [
        {
            "date": "1922-10-01",
            "title": "出生于安徽合肥",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1938",
            "title": "考入西南联合大学物理系",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1942",
            "title": "获西南联大学士学位",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1944",
            "title": "获清华大学研究院理科硕士",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1945",
            "title": "赴美留学，入芝加哥大学",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1948",
            "title": "获芝加哥大学哲学博士",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1949",
            "title": "入普林斯顿高等研究院",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1954",
            "title": "与米尔斯提出杨-米尔斯理论",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1956",
            "title": "与李政道提出宇称不守恒定律",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1957",
            "title": "获诺贝尔物理学奖",
            "category": "荣誉",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1964",
            "title": "加入美国国籍",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1966",
            "title": "任纽约州立大学石溪分校教授",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1971",
            "title": "首次回国访问，成为首位访华的海外华人科学家",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "1973",
            "title": "受到毛泽东接见",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1"
            ]
        },
        {
            "date": "1986",
            "title": "创立南开数学研究所理论物理研究室",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1"
            ]
        },
        {
            "date": "1999",
            "title": "退休回国，任清华大学高等研究中心名誉主任",
            "category": "教育",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2004",
            "title": "与翁帆结婚",
            "category": "出生",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2015",
            "title": "放弃美国国籍，转为中国科学院院士",
            "category": "政治",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "date": "2025-10-18",
            "title": "在北京逝世，享年103岁",
            "category": "逝世",
            "importance": "major",
            "confidence": "high",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "sources": [
        {
            "id": "S1",
            "title": "杨振宁",
            "publisher": "维基百科",
            "url": "https://zh.wikipedia.org/wiki/杨振宁",
            "tier": "wikipedia"
        },
        {
            "id": "S2",
            "title": "Yang Chen-Ning",
            "publisher": "Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Yang_Chen-Ning",
            "tier": "wikipedia"
        }
    ],
    "life_stages": [
        {
            "period": "1922-1945",
            "age_range": "0-23岁",
            "title": "战乱中求学",
            "description": "生于合肥，抗战中就读西南联大，获清华硕士后赴美。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1945-1966",
            "age_range": "23-44岁",
            "title": "美国学术巅峰",
            "description": "芝加哥大学博士，普林斯顿高等研究院，提出杨-米尔斯理论和宇称不守恒。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1966-1999",
            "age_range": "44-77岁",
            "title": "石溪分校与桥接中美",
            "description": "任石溪分校教授，1971年首次回国，成为中美学术交流桥梁。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1999-2025",
            "age_range": "77-103岁",
            "title": "回国晚年",
            "description": "退休回国任清华教授，放弃美国国籍转为中科院院士。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "turning_points": [
        {
            "period": "1945年",
            "title": "赴美留学",
            "choice": "考取庚款留美公费生赴芝加哥大学。",
            "consequence": "师从费米和特勒，走上理论物理研究之路。",
            "dark_side_or_failure": "离开战乱中的祖国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1954年",
            "title": "提出杨-米尔斯理论",
            "choice": "与米尔斯提出非阿贝尔规范场论。",
            "consequence": "成为粒子物理标准模型的基础。",
            "dark_side_or_failure": "当时未被物理学界充分重视。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1956年",
            "title": "提出宇称不守恒",
            "choice": "与李政道合作提出弱相互作用中宇称不守恒。",
            "consequence": "次年获诺贝尔物理学奖，成为首位获奖华人。",
            "dark_side_or_failure": "后与李政道因归属权争议决裂。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "2015年",
            "title": "放弃美国国籍回国",
            "choice": "放弃美国国籍，转为中国科学院院士。",
            "consequence": "全职回国投身科研与教育。",
            "dark_side_or_failure": "引发关于国籍选择的争议。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "timeline_sidebar": {
        "title": "关键线索",
        "items": [
            {
                "label": "最高荣誉",
                "value": "诺贝尔物理学奖",
                "description": "1957年获诺贝尔物理学奖，首位华人获奖者",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "核心理论",
                "value": "杨-米尔斯理论",
                "description": "非阿贝尔规范场论，粒子物理标准模型基础",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "label": "国籍变化",
                "value": "美国→中国",
                "description": "1964年入美籍，2015年放弃美籍转中国院士",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "achievement_controversy_brief": {
        "items": [
            {
                "type": "achievement",
                "label": "成就",
                "title": "诺贝尔物理学奖",
                "description": "与李政道共同提出宇称不守恒定律，1957年获诺贝尔物理学奖。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "type": "achievement",
                "label": "成就",
                "title": "杨-米尔斯理论",
                "description": "提出非阿贝尔规范场论，成为粒子物理标准模型的基础。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "type": "controversy",
                "label": "争议",
                "title": "与李政道之争",
                "description": "与李政道因宇称不守恒发现归属权产生分歧，最终决裂。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "relationship_network": {
        "center": "杨振宁",
        "center_note": "核心关系圈",
        "nodes": [
            {
                "name": "李政道",
                "type": "competitor",
                "relation": "合作者转对手",
                "description": "共同提出宇称不守恒并获诺贝尔奖，后因归属权争议决裂。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "费米",
                "type": "collaborator",
                "relation": "博士导师",
                "description": "芝加哥大学博士导师，著名物理学家。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "杜致礼",
                "type": "collaborator",
                "relation": "第一任妻子",
                "description": "杜聿明之女，1950年结婚，2003年逝世。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "name": "翁帆",
                "type": "collaborator",
                "relation": "第二任妻子",
                "description": "2004年结婚，年龄差54岁引发关注。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "era_map": [
        {
            "period": "1922-1945",
            "title": "战乱与求学",
            "context": "中国处于抗战时期。",
            "breakthrough": "在西南联大完成本科和硕士教育。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1945-1970",
            "title": "美国理论物理黄金时代",
            "context": "战后美国物理学蓬勃发展。",
            "breakthrough": "提出杨-米尔斯理论和宇称不守恒，获诺贝尔奖。",
            "source_ids": [
                "S1",
                "S2"
            ]
        },
        {
            "period": "1971-2025",
            "title": "中美学术桥梁与回国",
            "context": "中美关系从对抗到建交到交流。",
            "breakthrough": "1971年首次回国，2015年放弃美籍全职回国。",
            "source_ids": [
                "S1",
                "S2"
            ]
        }
    ],
    "influence_legacy": {
        "items": [
            {
                "dimension": "物理",
                "title": "杨-米尔斯理论",
                "description": "非阿贝尔规范场论成为粒子物理标准模型的基础，影响整个理论物理学。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "荣誉",
                "title": "首位华人诺贝尔奖",
                "description": "1957年获诺贝尔物理学奖，激励了整整一代华人科学家。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            },
            {
                "dimension": "教育",
                "title": "中美学术交流桥梁",
                "description": "1971年首次回国开启中美学术交流，晚年回国推动清华物理学科建设。",
                "source_ids": [
                    "S1",
                    "S2"
                ]
            }
        ]
    },
    "growth_curves": [
        {
            "title": "学术影响力",
            "description": "从西南联大到诺贝尔奖的学术轨迹。",
            "points": [
                {
                    "period": "1938",
                    "label": "西南联大",
                    "value": 10
                },
                {
                    "period": "1945",
                    "label": "赴美",
                    "value": 25
                },
                {
                    "period": "1948",
                    "label": "博士",
                    "value": 40
                },
                {
                    "period": "1954",
                    "label": "杨-米尔斯",
                    "value": 70
                },
                {
                    "period": "1957",
                    "label": "诺贝尔奖",
                    "value": 95
                },
                {
                    "period": "1971",
                    "label": "首次回国",
                    "value": 85
                },
                {
                    "period": "2015",
                    "label": "放弃美籍",
                    "value": 80
                }
            ]
        }
    ],
    "epitaph": {
        "text": "首位获诺贝尔奖的华人科学家，以杨-米尔斯规范场论奠定粒子物理标准模型基石，架起中西科学交流桥梁，二十世纪后半叶最具影响力的理论物理学家之一。",
        "source_ids": [
            "S1",
            "S2"
        ]
    },
    "uncertainty_notes": [
        "出生日期在1945年护照上被误记为9月22日。",
        "与李政道的决裂细节双方说法不一。"
    ],
    "source_notes": [
        "以维基百科（中英文）为主要来源。",
        "杨振宁于2025年10月18日在北京逝世。"
    ]
},

}


def get_person(name: str) -> dict | None:
    return PERSON_DB.get(name)


if __name__ == "__main__":
    import sys, json
    if len(sys.argv) < 2:
        print(f"Usage: python person_db.py <name>\nAvailable: {', '.join(PERSON_DB.keys())}", file=sys.stderr)
        sys.exit(1)
    name = sys.argv[1]
    person = get_person(name)
    if not person:
        print(f"Person '{name}' not found in database.", file=sys.stderr)
        print(f"Available: {', '.join(PERSON_DB.keys())}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(person, ensure_ascii=False, indent=2))

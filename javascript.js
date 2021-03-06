var procedures = [
  'Absent voting',
  'Addresses for papers',
  'Addresses for returns',
  'Addresses to the Crown',
  'Adjournment',
  'Adjournment debates',
  'Allocation of time and programming',
  'Allocation of time motions',
  'Allowances',
  'Amendment of the law motions',
  'Amendments and new clauses',
  'Amendments to questions',
  'Amendments to questions made',
  'Amendments to questions negatived',
  'Backbench Business Committee',
  'Backbench debates',
  'Ballot bills',
  'Bills',
  'Bills passed through several stages in one day',
  'Budgets',
  'Business motions',
  'Business questions',
  'Business statements',
  'By-election writs',
  'Campaigns',
  'Carry over motions',
  'Carry-over of bills',
  'Censure motions',
  'Chair of Committees of the Whole House',
  'Chairman of Ways and Means',
  'Church of England',
  'Clerk of the House',
  'Clerks at the Table',
  'Closure motions',
  'Closure of debate',
  'Clothing',
  'Committee of Selection',
  'Committee of the Whole House',
  'Committee proceedings',
  'Committee stage',
  'Commons amendments',
  'Commons messages',
  'Commons reasons',
  'Conduct',
  'Consent motions',
  'Consequential consideration stage',
  'Consolidation Bills Joint Select Committee',
  'Death',
  'Debates',
  'Debates adjourned and debates resumed',
  'Deferred divisions',
  'Delegated legislation',
  'Delegated Legislation Committee proceedings',
  'Deputy Speakers',
  'Devolution',
  'Digital debates',
  'Disallowed questions',
  'Disqualification',
  'Dissolution',
  'Divisions',
  'Early day motions',
  'Elections',
  'Emergency debates',
  'English votes for English laws',
  'e-petition debates',
  'e-petitions',
  'Estimates days',
  'European scrutiny and information',
  'European Scrutiny Select Committee',
  'Examiners of Petitions for Private Bills',
  'Explanatory notes',
  'Financial procedure',
  'First reading',
  'Freedom of expression',
  'General committees',
  'Government bills',
  'Government defeats',
  'Grand Committee proceedings (HC)',
  'Henry VIII clauses',
  'HL Standing Order No 10',
  'HL Standing Order No 10(5)',
  'HL Standing Order No 10A',
  'HL Standing Order No 11',
  'HL Standing Order No 127',
  'HL Standing Order No 13',
  'HL Standing Order No 139',
  'HL Standing Order No 15',
  'HL Standing Order No 150A',
  'HL Standing Order No 150B',
  'HL Standing Order No 151',
  'HL Standing Order No 154',
  'HL Standing Order No 155',
  'HL Standing Order No 156',
  'HL Standing Order No 157',
  'HL Standing Order No 159',
  'HL Standing Order No 16',
  'HL Standing Order No 166',
  'HL Standing Order No 167',
  'HL Standing Order No 17',
  'HL Standing Order No 171',
  'HL Standing Order No 172',
  'HL Standing Order No 18',
  'HL Standing Order No 18A',
  'HL Standing Order No 19',
  'HL Standing Order No 20',
  'HL Standing Order No 21',
  'HL Standing Order No 22',
  'HL Standing Order No 24',
  'HL Standing Order No 26',
  'HL Standing Order No 27',
  'HL Standing Order No 27A',
  'HL Standing Order No 29',
  'HL Standing Order No 30',
  'HL Standing Order No 31',
  'HL Standing Order No 32',
  'HL Standing Order No 34',
  'HL Standing Order No 37',
  'HL Standing Order No 38',
  'HL Standing Order No 39',
  'HL Standing Order No 40',
  'HL Standing Order No 41',
  'HL Standing Order No 42',
  'HL Standing Order No 43',
  'HL Standing Order No 44',
  'HL Standing Order No 45',
  'HL Standing Order No 46',
  'HL Standing Order No 47',
  'HL Standing Order No 48',
  'HL Standing Order No 49',
  'HL Standing Order No 4A',
  'HL Standing Order No 5',
  'HL Standing Order No 56',
  'HL Standing Order No 62',
  'HL Standing Order No 63',
  'HL Standing Order No 64',
  'HL Standing Order No 65',
  'HL Standing Order No 67',
  'HL Standing Order No 68A',
  'HL Standing Order No 70',
  'HL Standing Order No 70A',
  'HL Standing Order No 71',
  'HL Standing Order No 72',
  'HL Standing Order No 73',
  'HL Standing Order No 74',
  'HL Standing Order No 75',
  'HL Standing Order No 76',
  'HL Standing Order No 78',
  'HL Standing Order No 79',
  'HL Standing Order No 80',
  'HL Standing Order No 81',
  'HL Standing Order No 82',
  'HL Standing Order No 87',
  'HL Standing Order No 8A',
  'HL Standing Order No 8B',
  'HL Standing Order No 9',
  'HL Standing Order No 91',
  'HL Standing Order No 98',
  'House of Commons',
  'House of Commons chamber',
  'House of Commons Commission',
  'House of Commons journal',
  'House of Commons Liaison Committee',
  'House of Lords',
  'House of Lords Commission',
  'Human Rights Joint Select Committee',
  'Hybrid bills',
  'Joint select committees',
  'Lapsed proceedings',
  'Legislation',
  'Legislative grand committees',
  'Legislative process',
  'Legislative stages',
  'Lords amendments',
  'Lords messages',
  'Lords reasons',
  'Maiden speeches',
  'Members',
  'Members interests',
  'Members suspension',
  'Membership',
  'Membership motions',
  'Messages',
  'Ministerial statements',
  'Monarchy',
  'Money bills',
  'Money resolutions',
  'Motions for the adjournment',
  'Motions to sit in private',
  'Names of CBT terms added for Journal index',
  'National Security Strategy Joint Select Committee',
  'New clauses',
  'New schedules',
  'Northern Ireland Grand Committee',
  'Oaths and affirmations',
  'Official report',
  'Opening of Parliament',
  'Opposition',
  'Opposition days',
  'Oral questions',
  'Oral statements',
  'Order of business',
  'Orders for papers',
  'Pairing',
  'Panel of Chairs',
  'Papers presented or laid by various persons',
  'Papers presented under other authorities',
  'Parliament',
  'Parliament Act 1911',
  'Parliament Act 1949',
  'Parliamentary papers',
  'Parliamentary privilege',
  'Parliamentary procedure',
  'Parliamentary proceedings',
  'Parliamentary questions',
  'Parliamentary session',
  'Parlt Commissioner for Standards',
  'Pay',
  'Pensions',
  'Personal statements',
  'Petitions',
  'Petitions Select Committee',
  'Points of order',
  'Postponed proceedings',
  'Powers',
  'Presentation bills',
  'Prime Ministers questions',
  'Prince of Waless consent',
  'Private bills',
  'Private business',
  'Private members bills',
  'Private members bills proceedings',
  'Proceedings or business interrupted by the Speaker',
  'Programme motions',
  'Prorogation',
  'Proxy voting',
  'Public appointments',
  'Public bill committees',
  'Public bills',
  'Publications and records',
  'Queens consent',
  'Queens recommendation',
  'Queens speech',
  'Queens speech debates',
  'Question not decided',
  'Reasoned amendments',
  'Recall of parliament',
  'Recess',
  'Recess motions',
  'Reform',
  'Regulation',
  'Report stage',
  'Resolutions',
  'Revival motions',
  'Royal assent',
  'Rules and courtesies',
  'Second reading',
  'Second Reading Committee proceedings',
  'Select Committee reports',
  'Select Committee statements',
  'Select committees',
  'Speaker',
  'Speakers casting vote',
  'Speakers certificates',
  'Speakers Committee on the Electoral Commission',
  'Speakers statements',
  'Special procedure orders',
  'Speeches',
  'Standing Order No 1',
  'Standing Order No 10',
  'Standing Order No 102',
  'Standing Order No 116',
  'Standing Order No 117',
  'Standing Order No 120',
  'Standing Order No 121',
  'Standing Order No 121A',
  'Standing Order No 124',
  'Standing Order No 13',
  'Standing Order No 130',
  'Standing Order No 131',
  'Standing Order No 134',
  'Standing Order No 14',
  'Standing Order No 142',
  'Standing Order No 143',
  'Standing Order No 144',
  'Standing Order No 145',
  'Standing Order No 146',
  'Standing Order No 147',
  'Standing Order No 148',
  'Standing Order No 149',
  'Standing Order No 15',
  'Standing Order No 150',
  'Standing Order No 151',
  'Standing Order No 152',
  'Standing Order No 152A',
  'Standing Order No 152B',
  'Standing Order No 152H',
  'Standing Order No 16',
  'Standing Order No 18',
  'Standing Order No 188B',
  'Standing Order No 191',
  'Standing Order No 22',
  'Standing Order No 24 applications',
  'Standing Order No 27',
  'Standing Order No 29',
  'Standing Order No 3',
  'Standing Order No 30',
  'Standing Order No 37',
  'Standing Order No 38',
  'Standing Order No 39',
  'Standing Order No 42',
  'Standing Order No 43',
  'Standing Order No 45',
  'Standing Order No 55',
  'Standing Order No 57',
  'Standing Order No 78',
  'Standing Order No 86',
  'Standing Order No 89',
  'Standing Order No 93',
  'Standing Order No 94',
  'Standing Order No 96',
  'Standing Order No 97',
  'Standing Order No 99',
  'Standing orders',
  'Standing Orders Committee',
  'Statements',
  'Statutory Instruments Joint Select Committee',
  'Sub judice rule',
  'Supply estimates',
  'Suspension motions',
  'Ten minute rule bills',
  'Ten minute rule motions',
  'Third reading',
  'Time limits on speeches',
  'Times of sittings',
  'Timetabling of bills',
  'Topical debates',
  'UK scrutiny of European material',
  'Unparliamentary expressions',
  'Urgent questions',
  'Valedictory speeches',
  'Ways and means',
  'Ways and means resolutions',
  'Welsh Grand Committee',
  'Westminster Hall sittings',
  'Written questions',
  'Written statements'
]

var roles = [
'Gentleman Usher of the Black Rod',
'Yeoman Usher of the Black Rod',
'Lady Usher of the Black Rod',
'Searjant-at-Arms',
'Deputy-Searjant-at-Arms',
'Lord Speaker',
'Deputy Speaker',
'Speaker of the House of Commons',
'Clerk of the House',
'Committee Clerk',
'Second Clerk',
'Principal Clerk of the Table Office',
'Clerk-at-the-Table',
'Principal Clerk',
'Clerk of Committees',
'Clerk of Legislation',
'Deputy Principal Clerk',
'Committee Specialist',
'Senior Clerk',
'Assistant to the Clerk',
'Clerk of Bills',
'Chairman of Ways and Means',
'Clerk of the Journals',
'First Deputy Chairman of Ways and Means',
'Second Deputy Chairman of Ways and Means'
]

function newQuote() {
  var randomNumber = Math.floor(Math.random() * (procedures.length));
  var randomNumber1 = Math.floor(Math.random() * (roles.length));
  document.getElementById('quoteDisplay').innerHTML = "Ask the <span>" + roles[randomNumber1] + "</span> about <span>" + procedures[randomNumber] + "</span>";
}

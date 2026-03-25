1774435983508 [node_modules/fastify/lib/hooks.ts:408] info: 		🌐 OPTIONS /api/v1/knowledge/repo/pull - Headers: {"host":"localhost:3002","pragma":"no-cache","cache-control":"no-cache","accept":"*/*","access-control-request-method":"POST","access-control-request-headers":"authorization,content-type","origin":"http://localhost","user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36","sec-fetch-mode":"cors","sec-fetch-site":"same-site","sec-fetch-dest":"empty","referer":"http://localhost/","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","x-forwarded-for":"172.66.128.70"}

1774435983511 [node_modules/fastify/lib/hooks.ts:408] info: 		🌐 POST /api/v1/knowledge/repo/pull - Headers: {"host":"localhost:3002","content-length":"92","pragma":"no-cache","cache-control":"no-cache","sec-ch-ua-platform":"\"Android\"","authorization":"[REDACTED]","user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36","accept":"application/json, text/plain, */*","sec-ch-ua":"\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Brave\";v=\"146\"","content-type":"application/json","sec-ch-ua-mobile":"?1","sec-gpc":"1","origin":"http://localhost","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"http://localhost/","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","x-forwarded-for":"172.66.128.70"}

1774435983841 [unknown:0] info: 		✅ Token verified for user: 778292c5-ff68-4fd0-b0a4-b06748e186b5

1774435984187 [unknown:0] info: 		✅ Super admin access granted: admin@admin.com
haproxy         

172.66.128.70:20369 [25/Mar/2026:10:53:03.509] fe_admin_api admin_api/admin1 0/0/0/2053/2053 200 272 - - ---- 6/4/0/0/0 0/0 "POST /api/v1/knowledge/repo/pull HTTP/1.1"
admin-server    

1774435985561 [unknown:0] error: 		❌ Pull error: Backend returned 400

1774435985564 [node_modules/fastify/lib/hooks.ts:269] warn: 		SLOW REQUEST DETECTED
Neo4j: Loaded 0 folder summaries (0 folders changed)

   Neo4j: Storing 0 FolderNodes...

   Neo4j: ✅ 0 FolderNodes created

   Neo4j: Storing FolderVersions...

   Neo4j: ✅ 0 FolderVersions created

   Neo4j: Computing hierarchy relationships...

   Neo4j: ✅ Hierarchy: 0 CONTAINS_FILE, 0 CONTAINS_FOLDER

   OrgKeyword nodes by type: HAS_KEYWORD=7, HAS_ONTOLOGY_CONCEPT=6, HAS_BUSINESS_ENTITY=3, HAS_SYSTEM_CAPABILITY=4, HAS_SIDE_EFFECT=3, HAS_CONFIG_DEPENDENCY=1, HAS_INTEGRATION_SURFACE=1, PROVIDES_CONTRACT=1, CONSUMES_CONTRACT=6, HAS_FUNCTION=1, HAS_IMPORT_EXTERNAL=11, HAS_DATA_FLOW_DIRECTION=1

   APPEARS_IN_FILE by type: HAS_KEYWORD=7, HAS_ONTOLOGY_CONCEPT=6, HAS_BUSINESS_ENTITY=3, HAS_SYSTEM_CAPABILITY=4, HAS_SIDE_EFFECT=3, HAS_CONFIG_DEPENDENCY=1, HAS_INTEGRATION_SURFACE=1, PROVIDES_CONTRACT=1, CONSUMES_CONTRACT=6, HAS_FUNCTION=1, HAS_IMPORT_EXTERNAL=11, HAS_DATA_FLOW_DIRECTION=1

   APPEARS_IN_FOLDER by type: 

   Neo4j: Storing OrgKeywords — 45 keywords, 45 file edges, 0 folder edges...

   📌 [Pass 1] Batch 1/1 (45 nodes)...

   ✅ Pass 1 complete: 45 OrgKeyword nodes

   🔗 [Pass 2a] Batch 1/1 (45 file edges)...

   ✅ Pass 2a complete: 45 APPEARS_IN_FILE → FileVersion relationships

   📊 [Pass 3] Batch 1/1 (45 keywords)...

   ✅ Pass 3 complete: Frequencies recalculated

   Neo4j: ✅ OrgKeywords: 45 nodes, 45 file rels, 0 folder rels

   Neo4j: Storing RepoSummary...


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Neo4jFlatStorage complete:

   FileNodes: 1

   FileVersions: 1

   FolderNodes: 0

   FolderVersions: 0

   CONTAINS_FILE: 0

   CONTAINS_FOLDER: 0

   OrgKeyword nodes: 45

   APPEARS_IN_FILE: 45

   APPEARS_IN_FOLDER: 0

   RepoSummary: true

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Neo4j flat storage complete: 1 files, 0 folders

PHASE 6.2: Neo4j Graph Storage — handled by flat analysis strategy

commit-tracker.json: 0 added, 0 modified, 0 deleted | 2,882 in, 2,243 out

📊 Stats written: 3,447 in / 4,300 out



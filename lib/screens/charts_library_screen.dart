import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_storage/firebase_storage.dart';
import '../services/storage_service.dart';

class ChartsLibraryScreen extends StatefulWidget {
  const ChartsLibraryScreen({Key? key}) : super(key: key);

  @override
  _ChartsLibraryScreenState createState() => _ChartsLibraryScreenState();
}

class _ChartsLibraryScreenState extends State<ChartsLibraryScreen> {
  final StorageService _storageService = StorageService();
  List<Map<String, dynamic>> _charts = [];
  bool _isLoading = true;
  String _searchQuery = '';

  @override
  void initState() {
    super.initState();
    _loadCharts();
  }

  Future<void> _loadCharts() async {
    try {
      setState(() {
        _isLoading = true;
      });

      final charts = await _storageService.getAllBirthCharts();
      setState(() {
        _charts = charts;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
      _showErrorSnackBar('Failed to load charts: $e');
    }
  }

  Future<void> _searchCharts(String query) async {
    if (query.isEmpty) {
      await _loadCharts();
      return;
    }

    try {
      setState(() {
        _isLoading = true;
      });

      final charts = await _storageService.searchBirthChartsByName(query);
      setState(() {
        _charts = charts;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
      _showErrorSnackBar('Failed to search charts: $e');
    }
  }

  Future<void> _deleteChart(String chartId) async {
    try {
      await _storageService.deleteBirthChart(chartId);
      await _loadCharts();
      _showSuccessSnackBar('Chart deleted successfully');
    } catch (e) {
      _showErrorSnackBar('Failed to delete chart: $e');
    }
  }

  void _showErrorSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.red,
      ),
    );
  }

  void _showSuccessSnackBar(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.green,
      ),
    );
  }

  void _showChartDetails(Map<String, dynamic> chart) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Chart Details'),
        content: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildDetailRow('Name', chart['person_name'] ?? 'N/A'),
              _buildDetailRow('Birth Date', chart['birth_date'] ?? 'N/A'),
              _buildDetailRow('Birth Time', chart['birth_time'] ?? 'N/A'),
              _buildDetailRow('Birth Place', chart['birth_place'] ?? 'N/A'),
              _buildDetailRow('Created', _formatTimestamp(chart['created_at'])),
              SizedBox(height: 16),
              if (chart['chart_image_url'] != null)
                ElevatedButton(
                  onPressed: () => _viewChartImage(chart['chart_image_url']),
                  child: Text('View Chart Image'),
                ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text('Close'),
          ),
        ],
      ),
    );
  }

  Widget _buildDetailRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 100,
            child: Text(
              '$label:',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
          Expanded(
            child: Text(value),
          ),
        ],
      ),
    );
  }

  String _formatTimestamp(dynamic timestamp) {
    if (timestamp == null) return 'N/A';

    if (timestamp is Timestamp) {
      return timestamp.toDate().toString().split('.')[0];
    }

    return timestamp.toString();
  }

  void _viewChartImage(String imageUrl) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => Scaffold(
          appBar: AppBar(
            title: Text('Birth Chart'),
            backgroundColor: Colors.orange,
          ),
          body: Center(
            child: InteractiveViewer(
              child: Image.network(
                imageUrl,
                loadingBuilder: (context, child, loadingProgress) {
                  if (loadingProgress == null) return child;
                  return Center(
                    child: CircularProgressIndicator(
                      value: loadingProgress.expectedTotalBytes != null
                          ? loadingProgress.cumulativeBytesLoaded /
                              loadingProgress.expectedTotalBytes!
                          : null,
                    ),
                  );
                },
                errorBuilder: (context, error, stackTrace) {
                  return Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.error, size: 64, color: Colors.red),
                        SizedBox(height: 16),
                        Text('Failed to load image'),
                        Text(error.toString()),
                      ],
                    ),
                  );
                },
              ),
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Birth Charts Library'),
        backgroundColor: Colors.orange,
        actions: [
          IconButton(
            icon: Icon(Icons.refresh),
            onPressed: _loadCharts,
          ),
        ],
      ),
      body: Column(
        children: [
          // Search Bar
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: TextField(
              decoration: InputDecoration(
                hintText: 'Search by name...',
                prefixIcon: Icon(Icons.search),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
                filled: true,
                fillColor: Colors.grey[100],
              ),
              onChanged: (value) {
                setState(() {
                  _searchQuery = value;
                });
                _searchCharts(value);
              },
            ),
          ),

          // Charts List
          Expanded(
            child: _isLoading
                ? Center(child: CircularProgressIndicator())
                : _charts.isEmpty
                    ? Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              Icons.folder_open,
                              size: 64,
                              color: Colors.grey,
                            ),
                            SizedBox(height: 16),
                            Text(
                              'No charts found',
                              style: TextStyle(
                                fontSize: 18,
                                color: Colors.grey[600],
                              ),
                            ),
                            if (_searchQuery.isNotEmpty)
                              Text(
                                'Try a different search term',
                                style: TextStyle(
                                  color: Colors.grey[500],
                                ),
                              ),
                          ],
                        ),
                      )
                    : ListView.builder(
                        itemCount: _charts.length,
                        itemBuilder: (context, index) {
                          final chart = _charts[index];
                          return Card(
                            margin: EdgeInsets.symmetric(
                              horizontal: 16,
                              vertical: 4,
                            ),
                            child: ListTile(
                              leading: CircleAvatar(
                                backgroundColor: Colors.orange,
                                child: Icon(
                                  Icons.person,
                                  color: Colors.white,
                                ),
                              ),
                              title: Text(
                                chart['person_name'] ?? 'Unknown',
                                style: TextStyle(fontWeight: FontWeight.bold),
                              ),
                              subtitle: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                      'Birth: ${chart['birth_date'] ?? 'N/A'}'),
                                  Text(
                                      'Place: ${chart['birth_place'] ?? 'N/A'}'),
                                ],
                              ),
                              trailing: PopupMenuButton(
                                itemBuilder: (context) => [
                                  PopupMenuItem(
                                    value: 'view',
                                    child: Row(
                                      children: [
                                        Icon(Icons.visibility),
                                        SizedBox(width: 8),
                                        Text('View Details'),
                                      ],
                                    ),
                                  ),
                                  PopupMenuItem(
                                    value: 'image',
                                    child: Row(
                                      children: [
                                        Icon(Icons.image),
                                        SizedBox(width: 8),
                                        Text('View Chart'),
                                      ],
                                    ),
                                  ),
                                  PopupMenuItem(
                                    value: 'delete',
                                    child: Row(
                                      children: [
                                        Icon(Icons.delete, color: Colors.red),
                                        SizedBox(width: 8),
                                        Text('Delete',
                                            style:
                                                TextStyle(color: Colors.red)),
                                      ],
                                    ),
                                  ),
                                ],
                                onSelected: (value) {
                                  switch (value) {
                                    case 'view':
                                      _showChartDetails(chart);
                                      break;
                                    case 'image':
                                      if (chart['chart_image_url'] != null) {
                                        _viewChartImage(
                                            chart['chart_image_url']);
                                      }
                                      break;
                                    case 'delete':
                                      _showDeleteConfirmation(chart);
                                      break;
                                  }
                                },
                              ),
                            ),
                          );
                        },
                      ),
          ),
        ],
      ),
    );
  }

  void _showDeleteConfirmation(Map<String, dynamic> chart) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Delete Chart'),
        content: Text(
          'Are you sure you want to delete the chart for ${chart['person_name']}? This action cannot be undone.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text('Cancel'),
          ),
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
              _deleteChart(chart['id']);
            },
            child: Text(
              'Delete',
              style: TextStyle(color: Colors.red),
            ),
          ),
        ],
      ),
    );
  }
}
